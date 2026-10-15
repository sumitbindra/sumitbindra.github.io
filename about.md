---
layout: post
title: About
---

I'm an applied AI engineer who builds production-grade multi-agent LLM and voice AI systems, backed by 15 years of experience in transportation data modeling and forecasting. I ship end-to-end AI applications—from multi-agent orchestration platforms to real-time voice agents—using Python, TypeScript, and modern AI frameworks.

## Current Work

### TransLink (Metro Vancouver, BC)
**Project Manager & Senior Transportation Data Modeler** | September 2019 – Present

- Co-developed TransLink's regional trip- and activity-based travel demand model in Python; delivered ridership forecasts for the Surrey-Langley SkyTrain extension and station- and line-level forecasts for the entire Metro Vancouver transit system
- Lead a multi-million-dollar household trip diary and screenline data program covering sensitive personal information from 65% of the region's households, owning the data flow from collection through model calibration and estimation
- Built supporting data pipelines in Python and Databricks
- Bridge technical teams and stakeholders through recurring model user group meetings, building consensus on methods and translating forecasts into clear recommendations for decision-makers
- Implementing LLMs and other innovative solutions in modeling and customer service

### Independent AI Application Development
**Applied AI Engineer** | January 2021 – Present

Building production-grade multi-agent LLM and voice AI applications:

**ouroAI** — Multi-agent CRM automation platform (238 commits, 28+ PRs)
- Built a Gemini-orchestrated platform where four specialized tool-calling agents (query, outreach, sync, reporting) run SMS, email, WhatsApp, and AI voice campaigns through Twilio, Resend, and ElevenLabs with AI-generated replies, human escalation, and CRM sync
- Replaced a 3-call prompt chain with a DSPy ChainOfThought pipeline (channel choice, escalation, reply generation), optimized with BootstrapFewShot on 89 labeled conversations to 88.9% accuracy on a held-out validation set
- Implemented hybrid retrieval (Gemini embeddings + BM25) over CRM contacts and per-account knowledge bases synced to voice agents
- Stack: React/TypeScript, FastAPI, Supabase (Postgres, Auth, RLS multi-tenancy), Docker on Railway, 50+ pytest files plus Vitest and Playwright E2E tests

**AI Voice Call Scheduler** — Inbound and outbound voice agents on ElevenLabs Conversational AI over Twilio numbers; signature-verified FastAPI webhooks handle scheduling, voicemail auto-reschedule, and CRM booking via server tools; Gemini analyzes each transcript for summary, sentiment, action items, and reschedule intent

**CICA (Construction/Insurance Document AI)** — Structured extraction from bid forms, specs, and proposals using OpenAI/Gemini with Pydantic/JSON-schema outputs, LlamaIndex RAG, Azure Document Intelligence and Reducto parsing; flags financial, schedule, scope, and legal discrepancies with an LLM-judged eval harness

**BrickNova AI** — Conversational real-estate investment assistant for Miami condos; Google ADK + Gemini orchestrator routes to specialist agents using tool calling for unit search, building comparison, ROI, and cost-to-own calculations; Next.js 15/TypeScript, FastAPI, Supabase, Railway

**Answr** — Conversational survey and interview applications (employee satisfaction, customer feedback, transit-rider research) built on OpenAI Assistants API and LlamaIndex workflows with LLM follow-up probing, analysis dashboards, and WebRTC voice versions; includes a multilingual (English/Spanish) HR project management app built within weeks of the Assistants API's November 2023 launch

Partnered with YC founders to translate early ideas into working products, turning fuzzy requirements into clear specs and shipped features. Build daily with AI coding agents (Claude Code, Codex, Cursor, Replit Agent) to ship tested, containerized services quickly.

## Previous Experience

### Resource Systems Group Inc. (RSG)
**Consultant & Data Analyst** | August 2011 – August 2019

White River Junction, VT (remote from Vancouver since 2016)

- Delivered statewide and regional travel demand models for Michigan, Tennessee, and North Carolina DOTs and MPOs (SMTC, GTC), working directly with client agency staff from scoping through implementation, training, and support
- Built machine learning trip generation models from large multi-agency travel surveys (bootstrapping, probabilistic sampling, GLMs) and intermodal freight components (rail, truck, port) in Python and R
- Cut statewide model runtime 30% through parallelization and efficiency improvements; added toll modeling, Value of Time sensitivity, and 13 vehicle classes; analyzed 100+ projects for multi-million-dollar prioritization
- Analyzed large-scale cellphone origin-destination datasets (presented at TRB 2016); built GTFS transit networks, INRIX speed validation, and post-processors producing agency-ready maps and analyses

## Education

**Master of Science, Civil Engineering**  
University of Connecticut | 2006 – 2007

**Bachelor of Technology, Civil Engineering**  
Indian Institute of Technology (IIT) Guwahati, India | 2001 – 2005

## Core Competencies

**AI & LLM Engineering**
- Multi-agent orchestration (Google ADK, tool/function calling)
- Voice AI (ElevenLabs Conversational AI, Twilio integration)
- RAG and hybrid retrieval (embeddings + BM25) with pgvector (Supabase)
- LLM evaluation frameworks and test harnesses for non-deterministic systems
- DSPy prompt optimization (88.9% accuracy on held-out validation set)
- MCP servers for domain-specific data access
- Structured extraction (Pydantic/JSON schema)
- LangChain, LlamaIndex
- Gemini, OpenAI (including Assistants API), Claude

**Development & Data Engineering**
- Languages: Python, TypeScript, SQL, R
- Frameworks: React, Next.js, FastAPI
- Data: Supabase/Postgres (Auth, RLS multi-tenancy), DuckDB, Parquet, Databricks, pandas, GeoPandas, scikit-learn
- Infrastructure: Docker, Railway, Modal (serverless)
- Testing: pytest, Vitest, Playwright
- AI Dev Tools: Claude Code, Codex, Cursor, Replit Agent

**Transportation & Mobility Data**
- Travel demand modeling: ActivitySim, AequilibraE, four-step models (gravity/IPF, MNL, Frank-Wolfe assignment), activity-based models
- TransCAD 6/7, GTFS
- Data sources: cellphone O-D, INRIX, household travel surveys, GPS traces
- Ridership and demand forecasting
- Geocoding (Google Maps Geocoding API)

**Communication & Delivery**
- Stakeholder discovery and scoping
- Translating domain problems into working software
- User training and adoption support
- Multi-million-dollar program leadership
- Distributed team coordination

**Currently Learning:** LLM fine-tuning, AWS, C++

## Publications

- **Using Cellphone O-D Data for Regional Travel Model Validation.** Annual Meeting of the Transportation Research Board, Washington, D.C. (2016)
- **Predicting Segment-Intersection Crashes with Land Development Data.** Transportation Research Record: Journal of the Transportation Research Board (2009). Co-authors: J. N. Ivan and Thomas Jonsson
- **Explaining Road Speeds with Spatial Lag and Spatial Error Regression Models.** 86th Annual Meeting, TRB (2007). Co-authors: J. K. Hackney, M. Bernard, and K. W. Axhausen

## Get in Touch

- [Resume (PDF)](/assets/resume/Sumit_Bindra_Resume.pdf)
- [LinkedIn](https://www.linkedin.com/in/sumitbindra/)
- [GitHub](https://github.com/sumitbindra)
- [Email](mailto:sumitbindra@gmail.com)
