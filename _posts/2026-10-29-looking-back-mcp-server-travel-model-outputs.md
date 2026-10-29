---
layout: post
title: "Looking back: why I built an MCP server for travel-model outputs"
date: 2026-10-29
series: looking-back
series_part: 13
---

This is a look back, written in 2026, at work from November 2025. By that point, the Model Context Protocol—introduced by Anthropic in late 2024—had become a common way to plug tools and data into LLM clients and IDE agents. It gave applications a standardized interface to domain-specific resources without requiring custom integrations for every client. That standardization made it practical to build once and use everywhere.

## The Problem

Travel-model outputs are opaque. A regional travel demand model produces trip tables, skim matrices (travel time, distance, cost between zones), and household/person data stored in formats like Parquet files and OMX (Open Matrix). These formats are efficient for modeling software but hard for non-modelers to query. Someone wanting to know "how many households in zone 5 made trips by transit" or "what's the average travel time from zone 3 to zone 10" would need to know SQL, understand the schema, and have the right libraries installed.

LLM applications could help with that—writing SQL on demand, interpreting results, generating charts—but they need structured access to the data. That's what the MCP server was for.

## What I Built

The server is called travel-mcp-server. It exposes 8 tools that an LLM client can invoke:

- **execute_sql**: Run arbitrary SQL queries against the data using DuckDB, which loads Parquet tables in memory at startup
- **query_trips_by_person**: Get all trips for a specific person ID
- **summarize_trips_per_person**: Aggregate trip counts across all persons
- **get_trip_statistics**: Return mode split, average trip length, peak travel times
- **query_zone_info**: Look up details about a specific zone
- **query_skim_matrix**: Pull travel time, distance, or cost between two zones from the OMX skims
- **get_data_dictionary**: Return the full data dictionary so the LLM understands table schemas, column names, and what the values mean
- **generate_figure**: Create bar, line, pie, scatter, or histogram charts using matplotlib; returns a base64-encoded PNG as MCP ImageContent that renders directly in the client

Here's an example of what a query looks like:

```sql
SELECT mode, COUNT(*) as trip_count
FROM trips
WHERE origin_zone = 5
GROUP BY mode
ORDER BY trip_count DESC;
```

The LLM writes that SQL, invokes `execute_sql` with it, and presents the results in plain language. Or it calls `generate_figure` to turn the results into a chart.

The server runs in Docker, uses stdio mode (communication over standard input/output), and connects to clients like VS Code through a configuration file. The README documents how to add it to `mcp-settings.json` and run it with `docker run -i --rm`.

## How It Evolved

I built the first version on November 26, 2025. It had 5 analysis tools, synthetic travel data (zones, households, persons, trips stored as CSV files), a YAML data dictionary, Docker packaging, VS Code integration docs, and a test suite with a data generation script. The data was randomly generated for demonstration: 20 zones, 100 households, 250 persons, 800 trips.

The next day, November 27, I made a major update. CSV files were replaced with Parquet for faster loading and smaller file size. I added OMX skim matrices (travel time, distance, cost) and two new tools: `execute_sql` (using DuckDB to query Parquet tables directly) and `query_skim_matrix` (to pull values from the OMX file). That made the server much more flexible—clients could write their own queries instead of being limited to pre-built analysis tools.

Later that same day, I added `generate_figure`. Before that, the server could only return data as text or tables. With matplotlib integration, it could produce visual outputs—bar charts of mode split, line charts of travel time by distance, histograms of trip length distribution. The figures are returned as base64-encoded PNGs wrapped in MCP's ImageContent type, so they display inline in the client without needing to write files to disk. I wrote 7 pytest tests to cover each chart type and make sure they rendered correctly.

## Why the Data Dictionary Matters

The data dictionary is stored in YAML and returned by the `get_data_dictionary` tool. It describes every table, every column, the data types, what the columns represent, and what the possible values mean. For example, the `trips` table has a `mode` column with values like `Drive Alone`, `Carpool`, `Transit`, `Walk`, `Bike`, `TNC`. The dictionary explains that.

Without the dictionary, an LLM would have to guess what columns exist, what they're called, and what the values mean. It might write SQL that refers to a column that doesn't exist or interpret `mode` as something other than travel mode. With the dictionary, the LLM can check the schema first, understand the domain, and write correct queries.

This matters more in travel modeling than in typical databases because the field uses domain-specific terminology. "Skim," "TAZ" (Traffic Analysis Zone), "O-D matrix" (origin-destination), "mode split"—these aren't universal terms. The data dictionary bridges that gap.

## What I Learned

Building the MCP server taught me that data access is as important as the data itself. Travel models produce valuable outputs, but if only the people who built the model can query them, their usefulness is limited. The MCP protocol made it possible to turn those outputs into something an LLM client could work with, and the data dictionary made the queries reliable.

The synthetic demo data (20 zones, 100 households, 250 persons, 800 trips) was enough to validate the concept and test the tools. Real travel-model outputs are larger and more complex, but the structure is the same: Parquet tables, OMX skims, and a schema that needs to be documented.

The decision to add `execute_sql` was the right one. Pre-built analysis tools cover common cases, but they can't anticipate every question. SQL gives the LLM the flexibility to answer questions I didn't think of when I wrote the server. The data dictionary makes that practical by teaching the LLM the schema and the domain.

More details about travel-mcp-server and other travel modeling projects are available on my [Projects page](/projects#travel-mcp-server). The code is open source and available at [github.com/sumitbindra/travel-mcp-server](https://github.com/sumitbindra/travel-mcp-server).
