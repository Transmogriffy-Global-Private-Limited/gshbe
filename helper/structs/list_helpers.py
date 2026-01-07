from typing import Optional, List
from pydantic import BaseModel


class HelperListOut(BaseModel):
    registration_id: str
    account_id: str

    city: Optional[str] = None
    area: Optional[str] = None
    job_type: Optional[str] = None

    preferred_service_ids: List[str] = []

    # experience numbers (COUNT)
    experience_count: int
