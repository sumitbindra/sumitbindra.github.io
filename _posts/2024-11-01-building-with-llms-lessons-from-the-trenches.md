---
layout: post
title: "Building with LLMs: Lessons from the Trenches"
date: 2024-11-01
---

After a year of building products on top of large language models, here are the lessons that cost me the most time to learn. These aren't theoretical -- they come from shipping real applications and watching them succeed or fail in production.

## 1. Prompts Are Code, Treat Them That Way

Early on, I treated prompts as casual text -- something you tweak in a notebook until it works. That approach falls apart fast. Prompts need version control, testing, and review just like any other code. A one-word change in a system prompt can completely alter agent behavior.

I now keep prompts in dedicated files, write tests against expected outputs for key scenarios, and review prompt changes with the same scrutiny as code changes. It sounds obvious in retrospect, but most teams I talk to are still editing prompts in their application code as string literals.

## 2. The Last 20% Takes 80% of the Effort

Getting an LLM-powered feature to work in a demo takes a weekend. Getting it to work reliably in production takes months. The gap is filled with edge cases: malformed inputs, ambiguous instructions, hallucinated outputs, rate limits, context window management, and graceful degradation when the model just gets it wrong.

Plan for this. Budget for this. If your timeline assumes demo-quality is production-quality, you're going to have a bad time.

## 3. Structured Outputs Change Everything

The single biggest improvement in my agent reliability came from moving to structured outputs. Instead of asking the model to respond in free text and then parsing it (a recipe for fragile regex and broken JSON), I use function calling and structured output schemas.

When the model knows it needs to return a specific JSON shape with specific fields, the failure rate drops dramatically. It also makes downstream code simpler and more testable. If you're building agents and not using structured outputs, start there.

## 4. Evaluation Is the Bottleneck

Building the agent is the fun part. Evaluating whether it actually works is the hard part. And without good evaluation, you're flying blind.

I've learned to invest in evaluation infrastructure early. This means:
- A curated set of test cases that cover normal, edge, and adversarial scenarios
- Automated scoring where possible (exact match, semantic similarity, tool use correctness)
- Human review for subjective quality
- Regression testing so that improvements in one area don't break another

The teams that ship reliable AI products are the ones that take evaluation as seriously as feature development.

## 5. Know When Not to Use an LLM

This might be the most important lesson. LLMs are amazing, but they're not always the right tool. If a task can be solved with a database query, a rule-based system, or a simple algorithm, do that instead. LLMs are expensive, slow, and non-deterministic compared to traditional code.

I use LLMs for the parts that genuinely need language understanding, reasoning, or flexibility. Everything else gets handled by conventional code. This hybrid approach is faster, cheaper, and more reliable than trying to make the LLM do everything.

## Looking Forward

The pace of improvement in LLMs is extraordinary. What required clever workarounds six months ago now works out of the box. But the fundamentals -- treating AI engineering with the same rigor as software engineering -- aren't going away. If anything, as these systems get more capable, disciplined engineering practices become more important, not less.

I'll keep sharing what I learn as I build. The best way to understand this technology is to ship things with it.
