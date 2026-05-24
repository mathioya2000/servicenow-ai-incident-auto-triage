import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def analyze_incident(incident):
    prompt = f"""
You are a senior ServiceNow ITSM incident triage analyst.

Analyze the incident and return ONLY valid JSON.
Do not include markdown.
Do not include explanation outside JSON.

Use this priority logic:
- Priority 1 - Critical: major outage, business-wide impact, patient safety, revenue systems down
- Priority 2 - High: multiple users or important department affected
- Priority 3 - Moderate: single user affected but work is impacted
- Priority 4 - Low: minor issue or informational request

Use realistic ServiceNow-style assignment groups.

Incident:
Short Description: {incident.short_description}
Description: {incident.description}
Current Category: {incident.category}

Return exactly this JSON structure:
{{
  "predicted_category": "string",
  "predicted_subcategory": "string",
  "suggested_assignment_group": "string",
  "recommended_priority": "string",
  "impact": "string",
  "urgency": "string",
  "business_impact": "string",
  "routing_reason": "string",
  "troubleshooting_steps": ["string"],
  "confidence_score": 0.0,
  "escalation_required": true
}}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a ServiceNow ITSM expert. Always return valid JSON only."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.1,
        response_format={"type": "json_object"}
    )

    content = response.choices[0].message.content

    try:
        return json.loads(content)
    except json.JSONDecodeError:
        return {
            "error": "AI response was not valid JSON",
            "raw_response": content
        }