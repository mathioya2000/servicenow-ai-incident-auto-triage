def analyze_incident(incident):
    return {
        "predicted_category": "Network",
        "predicted_subcategory": "VPN",
        "suggested_assignment_group": "Network Support",
        "recommended_priority": "2 - High",
        "business_impact": "Remote employees may be unable to access company systems, affecting productivity and service delivery.",
        "troubleshooting_steps": [
            "Check VPN gateway status",
            "Review authentication logs",
            "Confirm if issue affects one user or multiple users",
            "Verify recent network or identity provider changes"
        ],
        "confidence_score": 0.86,
        "escalation_required": True
    }