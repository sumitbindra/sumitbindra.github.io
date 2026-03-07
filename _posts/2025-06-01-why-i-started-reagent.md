---
layout: post
title: "Why I Started ReAgent"
date: 2025-06-01
---

For the past year, I've been obsessed with a simple question: what would it take to build AI agents that actually work? Not demo-ware that looks impressive in a tweet thread, but agents that reliably complete real tasks in messy, real-world environments.

That question led me to start ReAgent.

## The Gap I Kept Seeing

I've spent years building startups -- from insurance AI to consumer apps to financial analysis tools. In every one of those ventures, there were workflows that were tedious, repetitive, and yet surprisingly hard to automate. Traditional software could handle the structured parts, but the moment you needed judgment, context, or the ability to handle unexpected situations, you were stuck writing endless if-else branches that never quite covered every case.

When GPT-4 and other frontier models arrived, I saw the missing piece. These models could reason. They could understand context. They could handle ambiguity. But wrapping them in a reliable agent framework -- one that could plan, execute, recover from errors, and actually finish the job -- that was (and still is) a hard engineering problem.

## Why Agents, Why Now

The timing matters. We're at a point where the underlying models are capable enough to be useful but the tooling and frameworks for building production agents are still immature. Most agent frameworks today are either too abstract (endless chains of prompt templates) or too rigid (hardcoded workflows with an LLM bolted on).

What I wanted was something in between: agents that have clear goals, can break down complex tasks into steps, use tools effectively, and know when to ask for help versus when to push forward. Agents that are transparent about what they're doing and why.

## What I Learned from Modeling Human Decisions

Here's where my unusual background comes in. Before startups and AI, I spent eight years building transportation demand models -- simulating how millions of people make daily travel decisions. Which route to take, which mode of transport, when to leave, whether to stop for coffee.

That work taught me something fundamental: modeling decision-making is about understanding trade-offs, constraints, and uncertainty. An agent deciding which API to call, how to parse a response, or when to retry a failed action is making decisions under uncertainty -- just like a commuter deciding whether to take the highway or surface streets.

The mathematical frameworks are different, but the intuition transfers. You need to think about choice sets, information availability, error recovery, and the cost of being wrong.

## What's Next

ReAgent is still early. I'm building in public where I can, sharing what works and what doesn't. The goal is to create agents that are useful today -- not waiting for AGI to arrive -- while building toward more capable autonomous systems.

If you're working on similar problems, or if you have workflows that feel like they should be automatable but aren't, I'd love to hear from you. The best products come from real problems, and I'm always looking for the next hard problem worth solving.

You can find me on [Twitter](https://twitter.com/MrSumitBindra) or [GitHub](https://github.com/sumitbindra).
