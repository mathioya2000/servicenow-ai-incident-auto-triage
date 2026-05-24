from fastapi import FastAPI
from app.models.incident import IncidentRequest
from app.services.triage_service import analyze_incident

app = FastAPI(
    title="ServiceNow AI Incident Auto-Triage API",
    description="AI-powered incident classification, priority recommendation, and routing assistant.",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "ServiceNow AI Incident Auto-Triage API is running"
    }


@app.post("/triage")
def triage_incident(incident: IncidentRequest):
    return analyze_incident(incident)