---
layout: post
title: "From Forecasting Models to AI Agents"
date: 2025-03-01
---

People often ask how I went from transportation modeling to building AI agents. On the surface, these seem like completely different fields. But the deeper I get into AI, the more I realize that my years of modeling complex systems were the perfect preparation.

## Modeling Millions of Decisions

At RSG, I built activity-based travel demand models -- large-scale simulations that predict how entire metropolitan populations move through their day. These models don't just forecast traffic volumes. They simulate individual decision-makers: when they leave home, where they go, what mode they choose, which route they take.

The core of this work is discrete choice modeling. You define a choice set (drive, bus, bike, walk), estimate a utility function for each option based on observable factors (travel time, cost, convenience), and add a stochastic error term because people are unpredictable. Then you simulate millions of these decisions and watch the system-level patterns emerge.

## The Connection to AI Agents

Here's what surprised me: building AI agents involves remarkably similar thinking.

**Choice architecture.** In travel models, you carefully define what options are available to each person based on their context. In agent design, you define what tools and actions are available at each step. Getting this right is critical -- too many options and the agent flounders, too few and it can't solve the problem.

**Sequential decisions.** Travel models simulate chains of decisions: first where to go, then when, then how. Each choice constrains the next. Agents work the same way -- each action changes the state of the world, and the next decision depends on what happened before.

**Handling uncertainty.** In travel modeling, you never have perfect information about why someone chose to drive instead of taking the bus. You model it probabilistically. Agents face the same challenge -- LLM outputs are stochastic, API calls can fail, and the environment changes unpredictably. Building robust systems means designing for uncertainty, not pretending it doesn't exist.

**Calibration and validation.** Travel models are calibrated against observed data -- actual traffic counts, survey responses, transit ridership. You can't just build a model and assume it works. Agents need the same rigor: systematic evaluation against ground truth, not just vibes-based testing.

## What Modeling Taught Me That AI Needs More Of

The transportation modeling community has decades of experience with a problem that AI is just starting to grapple with: how do you validate a complex system that makes thousands of interdependent decisions?

In travel modeling, we learned the hard way that a model can match aggregate statistics perfectly while being completely wrong at the individual level. The same risk exists with agents. An agent might complete a benchmark task correctly while using a fragile strategy that falls apart with slight variations.

The discipline of systematic validation -- testing at multiple levels, checking for the right reasons not just right answers, and being honest about what your system can't do -- is something I carry directly from modeling into my AI work.

## A Non-Linear Path

My career path from IIT Guwahati to UConn to transportation consulting to serial entrepreneurship to AI agents is anything but linear. But I've come to see that as a strength. Each phase built intuitions that the others couldn't have.

The modeling years gave me mathematical rigor and systems thinking. The startup years gave me product sense and bias toward shipping. And now, building AI agents, I get to combine both: rigorous thinking about complex systems, applied to products that actually solve problems.

The best AI work I've seen comes from people who bring deep domain expertise from outside AI. The field needs more of that cross-pollination.
