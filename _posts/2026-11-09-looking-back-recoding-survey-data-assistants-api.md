---
layout: post
title: "Looking back: recoding survey data with the OpenAI Assistants API"
date: 2026-11-09
series: looking-back
series_part: 1
---

This is a look back, written in 2026, at work from September to October 2024. By that point, OpenAI had shipped Structured Outputs and the gpt-4o-2024-08-06 model in August 2024, giving developers schema-constrained responses that made extraction practical without brittle parsing. The Assistants API—with Code Interpreter and file attachments—was OpenAI's main agent-style API at the time. In 2025, OpenAI shifted developers toward the Responses API and announced the Assistants API's deprecation, but in fall 2024, it was what we had.

## The Problem

I was working on a prototype to recode survey data. The data lived in a Supabase table, and the goal was to let someone specify a recoding request in plain English and have it applied to a column. For example: "recode the age to the following categories: 0 to 18, 18 to 65 and 65+". Or: "extract user origin and destination location" from a trip details column.

The repository for this work is private, so I won't link to it. But it was a Python CLI that took a table name, a column name, and a plain-English query, then wrote the recoded values back into a new column in the same table.

## Two Approaches

I tried two approaches to solve the problem.

**Approach A** used gpt-4o-2024-08-06's Structured Outputs. The CLI sent the recoding request to the model, which returned a categorization schema as JSON: type (sentiment, range, or custom), and either range definitions (name, description, lower bound, upper bound) or option definitions. That schema was then used to build a dynamic Pydantic model using `create_model`. Each row's value was classified one call per row against that model. The classified values went into a new column, and a YAML data dictionary was updated to document it.

Here's the idea:

```python
from pydantic import create_model

# Model returns categorization schema
categories = {
    "0-18": {"lower": 0, "upper": 18},
    "18-65": {"lower": 18, "upper": 65},
    "65+": {"lower": 65, "upper": None}
}

# Build dynamic Pydantic model from the schema
AgeCategory = create_model(
    "AgeCategory",
    category=(str, ...)
)

# Then classify each row value with one API call per row
```

**Approach B** used the Assistants API with Code Interpreter. The CLI pulled the whole table as a CSV, uploaded it to OpenAI's file storage (replacing any old file with the same name), and created or reused an Assistant called "Data Analyst for \<table\>" on gpt-4o with Code Interpreter and the file attached. The instructions told it to analyze the data, recode as requested, never edit the original columns, and save the result as a new CSV. The CLI created a thread, sent the recoding request, polled until the run completed, then sent a second message asking the Assistant to save the modified data as a CSV and return the file ID. The file ID was read from the message attachments, the CSV was downloaded, and the last column was extracted and added to the Supabase table via an RPC call (`add_column_to_table`), appending `_categorized` to the column name if it already existed.

## Five-Step Pipeline

Approach B, the Assistants API path, used a step tracker to manage progress and retry logic:

```
Step 1: Sync from Supabase (pull table to CSV)
Step 2: Create/update Assistant (upload file, attach to Assistant)
Step 3: Analysis (thread + run with recoding request)
Step 4: File creation (ask Assistant to save modified CSV)
Step 5: Sync to Supabase (download CSV, extract new column, upsert)
```

The tracker allowed up to 3 retry attempts, skipping steps that had already completed. This mattered when a run failed midway or when the model's response needed another attempt.

## What I Learned

The two approaches represented different trade-offs. Approach A gave fine-grained control: each row was classified individually, the Pydantic schema validated the output, and I could inspect every decision. But it scaled poorly—one API call per row meant higher latency and cost for large tables. Approach B handed the whole table to the model and let it write pandas code to recode everything in one pass. It was faster and cheaper, but less transparent: I couldn't see the intermediate steps unless I inspected the code the model generated.

Retry logic mattered. Models don't always return usable output on the first try, especially when they're generating code that needs to run. The step tracker let the system recover from failures without redoing work that had already succeeded.

Writing a new column instead of overwriting the original was a deliberate choice. It preserved the source data and made it easier to compare results, which mattered when evaluating whether the recoding was correct.

The project also connected to earlier work I'd done building conversational survey applications on the Assistants API. Those applications used LLM-driven follow-up probing and adaptive interviews. The recoding tool extended that concept: instead of asking questions, it transformed data based on instructions.

Looking back from 2026, the Assistants API's deprecation in favor of the Responses API makes this work feel like a snapshot of a specific moment. The API was the right tool at the time, but the landscape moved. What stayed constant was the need for structured extraction, retry logic, and preserving the original data—principles that carried forward into later work.

More posts in this series are available on the [Looking back series index](/looking-back/).
