from typing import Optional, List, Union
from pydantic import BaseModel
from uuid import UUID


# -------------------------
# PERSONAL HELPER RESPONSE
# -------------------------
class HelperPersonalOut(BaseModel):
    registration_id: UUID
    type: str = "personal"

    name: str
    age: Optional[int] = None
    faith: Optional[str] = None
    languages: Optional[str] = None

    city: str
    area: str
    phone: Optional[str] = None

    years_of_experience: Optional[int] = None
    avg_rating: Optional[float] = None
    rating_count: int


# -------------------------
# INSTITUTIONAL HELPER RESPONSE
# -------------------------
class HelperInstitutionalOut(BaseModel):
    registration_id: UUID
    type: str = "institutional"

    name: str
    city: str
    address: str
    phone: Optional[str] = None

    avg_rating: Optional[float] = None
    rating_count: int


# -------------------------
# UNION RESPONSE
# -------------------------
HelperListResponse = List[
    Union[
        HelperPersonalOut,
        HelperInstitutionalOut,
    ]
]
