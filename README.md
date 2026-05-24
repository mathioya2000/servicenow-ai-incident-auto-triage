# ServiceNow AI Incident Auto-Triage & Intelligent Routing Assistant

## Overview

An AI-powered ServiceNow incident triage automation platform that analyzes incoming incidents, determines business impact, recommends priority, routes incidents to the correct assignment group, and automatically assigns technicians using round-robin workload balancing.

This project demonstrates enterprise ServiceNow + AI integration using FastAPI, OpenAI, REST APIs, Business Rules, GlideRecord, and intelligent routing logic.

---

## Business Problem

Traditional incident triage is manual, inconsistent, and slow.

Common challenges:

- incorrect assignment groups
- delayed incident routing
- inconsistent prioritization
- overloaded technicians
- slow response times
- SLA breaches
- lack of business impact reasoning

This project automates those decisions using AI.

---

## Solution

This solution integrates ServiceNow with an AI decision engine that:

- analyzes incident descriptions
- classifies incidents
- determines business impact
- recommends ServiceNow priority
- maps incidents to correct assignment groups
- assigns technicians using round-robin logic
- updates incidents automatically

---

## Key Features

### AI Incident Classification
Examples:

- Email outage
- VPN access failures
- Phishing/security incidents
- Software/application issues
- Database incidents
- Clinical/EMR incidents

---

### Intelligent Priority Recommendation

Automatically aligns AI recommendations to ServiceNow priority matrix.

Example:

AI recommends:

Priority 2 - High

ServiceNow updates:

- Impact = 1 - High
- Urgency = 2 - Medium
- Priority = 2 - High

---

### Intelligent Assignment Group Routing

Examples:

| Incident Type | Assignment Group |
|--------------|------------------|
| Email / Messaging | Service Desk |
| VPN / Network | Network Support |
| Security / Phishing | Security Team |
| Database | Database |
| Clinical / EMR | Clinical IT Support |
| Software | Software |
| Change | Change Management |
| Problem | Problem Solving |

---

### Round-Robin Technician Assignment

Automatically distributes incidents fairly:

Incident 1 → Technician A  
Incident 2 → Technician B  
Incident 3 → Technician C  
Incident 4 → Technician A

Prevents technician overload.

---

### ServiceNow Auto Updates

Automatically updates:

- Assignment Group
- Assigned To
- Priority
- Impact
- Urgency
- Work Notes
- SLA activation

---

## Architecture

```text
ServiceNow Incident
        ↓
Business Rule
        ↓
REST Message
        ↓
ngrok Public Endpoint
        ↓
FastAPI Backend
        ↓
OpenAI Decision Engine
        ↓
JSON Structured Response
        ↓
ServiceNow Updates:
  - Priority
  - Impact
  - Urgency
  - Assignment Group
  - Assigned Technician
  - Work Notes
  - SLA
```

---

## Technology Stack

### ServiceNow
- Business Rules
- RESTMessageV2
- GlideRecord
- Incident Management
- Assignment Group Routing
- Round-Robin Automation
- SLA Engine

### Backend
- Python
- FastAPI
- Uvicorn

### AI
- OpenAI API
- Prompt Engineering
- Structured JSON Responses

### Integration
- REST APIs
- ngrok

---

## API Example

### Request

```json
{
  "short_description": "VPN login failures",
  "description": "Multiple remote employees cannot connect after password reset",
  "category": "network"
}
```

### Response

```json
{
  "predicted_category": "Network",
  "predicted_subcategory": "VPN",
  "suggested_assignment_group": "Network Operations",
  "recommended_priority": "Priority 2 - High",
  "impact": "Multiple users affected",
  "urgency": "High",
  "business_impact": "Remote work capabilities impacted",
  "routing_reason": "Multiple VPN failures detected",
  "confidence_score": 0.85
}
```

---

## Screenshots

Add screenshots here:

- Swagger API test
- ServiceNow incident before AI
- ServiceNow incident after AI triage
- Assignment group routing
- Round-robin assignment
- SLA activation

---

## Business Value

This solution improves:

- faster triage
- better routing accuracy
- fair technician workload distribution
- improved SLA compliance
- reduced manual effort
- faster incident response

---

## Interview Talking Points

This project demonstrates:

- ServiceNow development
- AI integration
- API design
- REST integrations
- business automation
- ITSM operational thinking
- assignment routing logic
- round-robin workload balancing
- enterprise architecture design

---

## Future Enhancements

- CMDB impact analysis
- CSDM service mapping
- incident similarity detection
- AI knowledge article suggestions
- incident clustering
- dashboard analytics
- deployment to cloud hosting