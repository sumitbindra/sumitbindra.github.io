---
layout: post
title: "Looking back: structured extraction with Pydantic and JSON schemas, the core of CICA"
date: 2026-10-26
series: looking-back
series_part: 10
---

This is a look back, written in 2026, at work from spring 2025—specifically March to June of that year. By early 2025, major model APIs had added the ability to constrain output to a JSON schema. OpenAI had introduced structured outputs in August 2024, and Gemini's API supported response schemas. That capability made schema-first extraction practical in a way it hadn't been before, and CICA was built around it.

## The Problem

Construction bidding involves comparing complex documents against each other. A specification says one thing about project scope, schedule, or pricing. A proposal or bid form says something else. The question is whether they match, and if not, whether the difference matters.

I built CICA to extract structured information from these documents—bid forms, ground truth proposals, specifications—and identify discrepancies. The discrepancies CICA looked for were financial, schedule, scope-related, and legal. The goal wasn't to make final decisions but to flag potential issues that someone needed to review.

## Questions Defined in YAML

The extraction process started with questions, defined in YAML. Each question had a key, a description, and tags for the types of documents it applied to (bid form, proposal, etc.) and the construction category it belonged to (general, financial, schedule, technical, scope, legal).

Here's what the structure looked like:

```yaml
question: What is the project start date?
key: project_start_date
description: The date when construction work is scheduled to begin
categories:
  - bid_form
  - ground_truth_proposal
construction_category: schedule
```

The questions gave the system a clear target for what to extract. Rather than asking a model to figure out what might be important in a document, I told it exactly what to look for.

## Pydantic Models and JSON Schemas

Once the questions were defined, I used Pydantic models to generate JSON schemas. The models described the shape of the answer: each field, its type, whether it was required. The schema was then passed to the model API, which constrained the response to match that structure.

Here's a simplified version of what the comparison output looked like:

```python
from pydantic import BaseModel

class ComparisonRecord(BaseModel):
    question: str
    specification_flag: bool
    specification: str
    proposal_flag: bool
    proposal: str
    difference_flag: bool
    difference: str
    implication: str
```

The `difference_flag` field was the key one. When set to true, it meant the system had identified a discrepancy worth reviewing. The frontend only displayed flagged differences, so reviewers could focus on what mattered.

## One Question at a Time

Early on, I made a choice that seemed counterintuitive: ask one question at a time instead of sending all the questions together. The README for CICA_API_v1 says it plainly: "Sending LLM one question at a time seems to perform better than sending all questions together."

I hedged that statement because I didn't have rigorous proof, just observation. My observation was that it performed better, and it also made failures easier to debug. The trade-off is more API calls and higher latency.

## Mixing OpenAI and Gemini

CICA used both OpenAI and Gemini. There was an environment flag that let me choose which model handled which part of the pipeline. I used one for general response extraction and the other for structured extraction.

## Parsing and Retry Logic

Document parsing was handled by Reducto, which turned PDFs and other formats into text the models could process. I also added Azure Document Intelligence as an option earlier in development. The system included a retry mechanism for when Gemini (or any model) failed to return a valid response. Rather than failing the whole job, it would try again, up to a configured limit.

This kind of plumbing—retries, error handling, fallback paths—took more time than the extraction logic itself. But it was necessary to make the system usable in practice, not just in controlled tests.

## Testing with pytest

The test harness was built with pytest. The tests compared outputs against expected results and used an LLM to judge whether the extraction was correct. This was necessary because the answers weren't always exact matches—they might be phrased differently but mean the same thing.

The test configuration was stored in a file called `tests_input.json`, and the results went into `test_results.json`, with pass/fail verdicts and explanations.

## What I Learned

Structured outputs changed the game. Before schema-constrained responses were widely available, extraction systems required brittle parsing logic, regex patterns that broke on edge cases, and constant manual cleanup. With schemas, the model did the heavy lifting, and the code became simpler and more reliable.

The lesson that stuck with me: don't ask models to do more than they need to. Define the task narrowly, give them a clear structure to fill in, and verify the results systematically. That discipline—treating LLM-based systems like any other software, with schemas, tests, and error handling—was what made CICA work.

More details about CICA and the full technical stack are available on my [Projects page](/projects#cica).
