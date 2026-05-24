import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def analyze_incident(incident):
    prompt = f"""
You are an expert ServiceNow ITSM incident triage assistant.

Analyze this incident and return ONLY valid JSON.

Incident:
Short Description: {incident.short_description}
Description: {incident.description}
Category: {incident.category}

Return:
{{
  "predicted_category": "",
  "predicted_subcategory": "",
  "suggested_assignment_group": "",
  "recommended_priority": "",
  "business_impact": "",
  "troubleshooting_steps": [],
  "confidence_score": 0.0,
  "escalation_required": false
}}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a ServiceNow ITSM expert."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    content = response.choices[0].message.content
    return json.loads(content)