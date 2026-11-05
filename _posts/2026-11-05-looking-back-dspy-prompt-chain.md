---
layout: post
title: "Looking back: Replacing a prompt chain with DSPy: 88.9% on held-out data"
date: 2026-11-05
series: looking-back
series_part: 17
---

This is a look back, written in 2026, at work from February to April 2026. By early 2026, teams building with LLMs were moving from hand-written prompts toward programmatic prompt optimization. DSPy had emerged as a practical tool: define signatures (input-output structure), write modules composing those signatures, and let optimizers like BootstrapFewShot and MIPROv2 learn better prompts from labeled examples. The promise was measurable, repeatable quality instead of guesswork.

## The Problem

Before DSPy, the conversation reply engine in ouroAI—a multi-agent CRM automation platform—used a 3-call prompt pipeline with Gemini:

1. **Channel decision**: Choose SMS, email, WhatsApp, or voice (ElevenLabs outbound call).
2. **Escalation decision**: Continue the conversation or escalate to a human (contact ready for a deal, highly engaged, or explicitly requesting a person).
3. **Message generation**: Write the reply text for the chosen channel.

The pipeline worked most of the time, but the escalation logic was fragile. False escalations—flagging routine messages as requiring human intervention—were the main errors. There was no systematic way to measure performance or improve it. When it failed, I tweaked prompts and hoped nothing else broke.

## Three DSPy Signatures with ChainOfThought

I replaced the 3-call pipeline with a DSPy module that used three signatures, each wrapped in `ChainOfThought`:

```python
# Simplified sketch of the DSPy conversation pipeline
class ConversationPipeline(dspy.Module):
    def __init__(self):
        super().__init__()
        self.channel_decision = dspy.ChainOfThought("context, conversation_history -> channel, reasoning")
        self.escalation_decision = dspy.ChainOfThought("context, conversation_history, channel -> should_escalate, should_continue, reasoning")
        self.message_generation = dspy.ChainOfThought("context, conversation_history, channel, escalation_decision -> message, reasoning")
    
    def forward(self, context, conversation_history):
        channel = self.channel_decision(context=context, conversation_history=conversation_history)
        escalation = self.escalation_decision(context=context, conversation_history=conversation_history, channel=channel.channel)
        message = self.message_generation(context=context, conversation_history=conversation_history, channel=channel.channel, escalation_decision=escalation)
        
        return dspy.Prediction(
            channel=channel.channel,
            should_escalate=escalation.should_escalate,
            should_continue=escalation.should_continue,
            message=message.message
        )
```

Each signature declared inputs and outputs. `ChainOfThought` instructed the LLM to reason before answering, improving accuracy on complex cases.

The same `generate_ai_response()` function signature was preserved, so an environment flag (`PROMPT_CONVERSATION_PIPELINE=true`) could switch back to the old pipeline. This let me run both side-by-side on the same scenarios.

## BootstrapFewShot and Weighted Metrics

BootstrapFewShot is a DSPy optimizer. It generates reasoning traces from training examples, selects high-quality traces as few-shot demonstrations, then recompiles the module to include those demonstrations in the prompts.

I had 89 labeled conversations with correct channel, escalation decision, and expected reply annotated. I split them 70/30: 62 for training, 27 for validation.

The metric was a weighted composite:

- **Channel decision**: 0.30 (exact match)
- **Escalation decision (should_escalate)**: 0.35 (exact boolean match)
- **Continuation decision (should_continue)**: 0.15 (exact boolean match)
- **Message quality**: 0.20 (non-empty string check only—I didn't have a rigorous way to grade message quality)

Escalation received the heaviest weight because false escalations were the biggest fragility in the old pipeline.

After optimization, BootstrapFewShot produced a module with 4 bootstrapped demonstrations and 4 labeled demonstrations. The optimized prompts were saved to a JSON file (`optimized_prompts/conversation_pipeline.json`) and loaded at runtime.

## Results

On the 27-example validation set, the DSPy pipeline achieved **88.9% accuracy**. All channel-switch scenarios scored 1.0. The remaining misses were escalation edge cases where the boundary between "engaged" and "deal-ready" was genuinely ambiguous.

To be clear: 27 validation examples is a small test set. The result isn't a claim of flawless performance at scale. It's evidence that DSPy optimization produced measurable improvement over hand-written prompts on the labeled data I had.

Message quality was the weakest part of the evaluation. The 0.20 weight reflected a non-empty check, not a judgment of tone or appropriateness—a limitation I accepted. Grading open-ended text rigorously would have required human review or an LLM judge I didn't implement. The pipeline generated reasonable responses in spot checks, which was enough for this stage.

## Earlier DSPy Uses in the Same Project

The conversation pipeline wasn't the first DSPy component in ouroAI. Two earlier modules had already shown the value of programmatic optimization:

**Planner optimization (February 14)**: A DSPy planner module decided which tools to call, in what order, and with what parameters. Baseline: 87.1% on 23 evaluation cases. After MIPROv2 optimization: 90.1%. The metric was a weighted composite of tool coverage, ordering, parameter quality, forbidden-tool avoidance, and step count.

**Contact search classifier (February 25)**: A teacher-student setup where Gemini Pro labeled a sample of 30 contacts, BootstrapFewShot optimized a Gemini Flash classifier, and Flash classified the rest in parallel. Result: 89% recall (81/91) on an eval set. The baseline code-generation pipeline: 3.3% recall (3/91).

These earlier wins made the case for bringing DSPy into the conversation pipeline. The pattern was consistent: labeled examples plus a clear metric produced better results than hand-written prompts.

## What I Learned

Structured prompt optimization changed how I thought about building with LLMs. Before DSPy, improving a pipeline meant manual iteration: tweak, test, check for breakage, repeat. With DSPy, it meant collecting labeled examples, defining a metric, and running an optimizer. The result was measurable and reproducible.

The weighted metric was the key design choice. Without it, the optimizer wouldn't have known that escalation mattered more than channel choice or that a non-empty message was a bare minimum. The metric encoded system priorities; the optimizer learned to meet them.

The 88.9% result on 27 held-out examples wasn't perfect, but it was concrete. I knew where the pipeline succeeded (channel decisions, most escalations) and where it struggled (edge cases). That clarity—backed by numbers—was something the hand-written pipeline never gave me.

More details about ouroAI and the full technical stack are available on my [Projects page](/projects#ouroai).
