from typing import List, Optional, Literal, Dict, Any
from pydantic import BaseModel, Field

Urgency = Literal["low", "medium", "high"]
Intent = Literal["request_quote", "request_info", "change_request", "complaint", "other"]
Format = Literal["in_person", "remote", "hybrid", "unknown"]

class SeminarNeeds(BaseModel):
    summary: str = Field(..., description="Résumé 3-6 lignes de la demande")
    intent: Intent
    urgency: Urgency

    # Basics
    company: Optional[str] = None
    contact_name: Optional[str] = None
    contact_email: Optional[str] = None

    # Seminar info
    seminar_title: Optional[str] = None
    format: Format = "unknown"
    location_city: Optional[str] = None
    location_country: Optional[str] = None
    venue_requirements: Optional[str] = None

    # Dates & duration
    preferred_dates: List[str] = Field(default_factory=list, description="Dates ou périodes mentionnées")
    duration_days: Optional[float] = None

    # People
    participants_count: Optional[int] = None
    participants_profile: Optional[str] = None
    language: Optional[str] = None

    # Objectives & content
    objectives: List[str] = Field(default_factory=list)
    topics: List[str] = Field(default_factory=list)

    # Budget
    budget_eur_min: Optional[int] = None
    budget_eur_max: Optional[int] = None
    budget_notes: Optional[str] = None

    # Constraints
    constraints: List[str] = Field(default_factory=list)

    # Stakeholders
    decision_makers: List[str] = Field(default_factory=list)
    stakeholders: List[str] = Field(default_factory=list)

    # Missing info / next steps
    missing_information: List[str] = Field(default_factory=list)
    recommended_next_action: str

    confidence: float = Field(..., ge=0.0, le=1.0)

    # For traceability
    extracted_entities: Dict[str, Any] = Field(default_factory=dict, description="Optionnel: indices/entités détectées")
