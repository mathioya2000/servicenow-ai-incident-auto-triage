# ServiceNow AI Incident Auto-Triage & Intelligent Routing

A ServiceNow portfolio project that uses AI to analyze incoming incidents, recommend priority, route work to the appropriate assignment group, and support faster incident resolution.

## Project Overview

Service desks often receive incidents with incomplete descriptions, incorrect priorities, and inconsistent assignment groups. This solution demonstrates how ServiceNow can integrate with an AI service to improve incident triage while keeping the final workflow inside ServiceNow.

## Key Features

- AI-assisted incident classification
- Priority recommendation based on impact and urgency
- Suggested assignment group
- Intelligent incident routing
- SLA-aware triage support
- Round-robin technician assignment
- Incident summarization
- Structured AI response handling
- ServiceNow record updates
- Error handling and processing-status tracking

## Workflow

1. An incident is created or updated in ServiceNow.
2. A Business Rule prepares the incident information.
3. RESTMessageV2 sends the incident data to the FastAPI service.
4. The FastAPI service sends a structured prompt to the OpenAI API.
5. The AI returns classification, priority, routing, and support recommendations.
6. ServiceNow processes the response using GlideRecord.
7. The incident is updated with the recommended triage information.

## Architecture

```text
ServiceNow Incident
        |
        v
Business Rule
        |
        v
RESTMessageV2
        |
        v
FastAPI Integration Service
        |
        v
OpenAI API
        |
        v
Structured AI Response
        |
        v
ServiceNow Incident Update
