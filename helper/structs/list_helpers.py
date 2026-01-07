from pydantic import BaseModel
from typing import Optional


class HelperListOut(BaseModel):
    registration_id: str
    name: str
    age: Optional[int]
    faith: Optional[str]
    languages: Optional[str]
    city: str
    area: str
    phone: Optional[str]
    years_of_experience: Optional[int]
    avg_rating: Optional[float]
    rating_count: int
