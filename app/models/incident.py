from pydantic import BaseModel


class IncidentRequest(BaseModel):
    short_description: str
    description: str
    category: str | None = None