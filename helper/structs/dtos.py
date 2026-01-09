from typing import List, Optional, Literal, Union
from pydantic import BaseModel, Field


# =====================================================
# COMMON
# =====================================================
'''
JobType = Literal["part_time", "full_time", "one_time", "subscription"]


class DeleteOut(BaseModel):
    deleted: bool = Field(True, examples=[True])'''


# =====================================================
# HELPER LIST (PUBLIC)
# =====================================================

'''class HelperPersonalProfileOut(BaseModel):
    registration: str
    name: str
    age: Optional[int] = None
    faith: Optional[str] = None
    languages: Optional[str] = None
    city: Optional[str] = None
    area: Optional[str] = None
    phone: Optional[str] = None
    years_of_experience: Optional[int] = None
    avg_rating: Optional[str] = None
    rating_count: Optional[int] = None


class HelperInstitutionalProfileOut(BaseModel):
    registration: str
    name: str
    city: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None
    avg_rating: Optional[str] = None
    rating_count: Optional[int] = None


class HelperListItemOut(BaseModel):
    registration_id: str
    role: Literal["helper"]
    capacity: Literal["personal", "institutional"]
    profile_kind: Literal["helper_personal", "helper_institutional"]
    profile: Union[
        HelperPersonalProfileOut,
        HelperInstitutionalProfileOut,
    ]


class HelperListOut(BaseModel):
    items: List[HelperListItemOut]


# =====================================================
# PREFERENCE
# =====================================================

class HelperPreferenceUpsertIn(BaseModel):
    city: Optional[str] = Field(None, examples=["Kolkata"])
    area: Optional[str] = Field(None, examples=["Salt Lake"])
    job_type: Optional[JobType] = Field(None, examples=["part_time"])
    preferred_service_ids: List[str] = Field(
        default_factory=list,
        description="Replaces the entire preferred services set",
        examples=[["b2b9c9c2-9d0b-4c6f-9e5b-2d4cefd1d5c1"]],
    )


class HelperPreferenceOut(BaseModel):
    registration_id: str
    city: Optional[str] = None
    area: Optional[str] = None
    job_type: Optional[str] = None
    preferred_service_ids: List[str] = Field(default_factory=list)


# =====================================================
# EXPERIENCE
# =====================================================

class HelperExperienceIn(BaseModel):
    year_from: Optional[int] = Field(None, ge=1900, le=2100, examples=[2019])
    year_to: Optional[int] = Field(None, ge=1900, le=2100, examples=[2024])
    service_id: Optional[str] = Field(None, description="Service.id")
    city: Optional[str] = Field(None, examples=["Kolkata"])
    area: Optional[str] = Field(None, examples=["Behala"])
    description: Optional[str] = Field(
        None,
        examples=["Worked as a home nurse for elderly patients."],
    )


class HelperExperienceOut(BaseModel):
    id: str
    registration_id: str
    year_from: Optional[int] = None
    year_to: Optional[int] = None
    service_id: Optional[str] = None
    city: Optional[str] = None
    area: Optional[str] = None
    description: Optional[str] = None'''
'''from __future__ import annotations
 
from typing import List, Optional, Literal, Union
from pydantic import BaseModel, Field'''
 
 
# =====================================================
# COMMON
# =====================================================
 
JobType = Literal["part_time", "full_time", "one_time", "subscription"]
 
 
class DeleteOut(BaseModel):
    deleted: bool = Field(True, examples=[True])
 
 
# =====================================================
# HELPER LIST (PUBLIC)
# =====================================================
 
class HelperPersonalProfileOut(BaseModel):
    id: str
    registration: str
    name: str
    age: Optional[int] = None
    faith: Optional[str] = None
    languages: Optional[str] = None
    city: Optional[str] = None
    area: Optional[str] = None
    phone: Optional[str] = None
    years_of_experience: Optional[int] = None
    avg_rating: Optional[str] = None
    rating_count: Optional[int] = None
 
 
class HelperInstitutionalProfileOut(BaseModel):
    id: str
    registration: str
    institution_name: str
    city: Optional[str] = None
    area: Optional[str] = None
    phone: Optional[str] = None
    avg_rating: Optional[str] = None
    rating_count: Optional[int] = None
 
 
class HelperListItemOut(BaseModel):
    registration_id: str
    role: Literal["helper"]
    capacity: Literal["personal", "institutional"]
    profile_kind: Literal["helper_personal", "helper_institutional"]
    profile: Union[
        HelperPersonalProfileOut,
        HelperInstitutionalProfileOut,
    ]
 
 
class HelperListOut(BaseModel):
    items: List[HelperListItemOut] = Field(default_factory=list)
 
 
# =====================================================
# PREFERENCE
# =====================================================
 
class HelperPreferenceUpsertIn(BaseModel):
    city: Optional[str] = Field(None, examples=["Kolkata"])
    area: Optional[str] = Field(None, examples=["Salt Lake"])
    job_type: Optional[JobType] = Field(None, examples=["part_time"])
    preferred_service_ids: List[str] = Field(
        default_factory=list,
        description="Replaces the entire preferred services set",
        examples=[["b2b9c9c2-9d0b-4c6f-9e5b-2d4cefd1d5c1"]],
    )
 
 
class HelperPreferenceOut(BaseModel):
    registration_id: str
    city: Optional[str] = None
    area: Optional[str] = None
    job_type: Optional[str] = None
    preferred_service_ids: List[str] = Field(default_factory=list)
 
 
# =====================================================
# EXPERIENCE
# =====================================================
 
class HelperExperienceIn(BaseModel):
    year_from: Optional[int] = Field(None, ge=1900, le=2100, examples=[2019])
    year_to: Optional[int] = Field(None, ge=1900, le=2100, examples=[2024])
    service_id: Optional[str] = Field(None, description="Service.id")
    city: Optional[str] = Field(None, examples=["Kolkata"])
    area: Optional[str] = Field(None, examples=["Behala"])
    description: Optional[str] = Field(
        None,
        examples=["Worked as a home nurse for elderly patients."],
    )
 
 
class HelperExperienceOut(BaseModel):
    id: str
    registration_id: str
    year_from: Optional[int] = None
    year_to: Optional[int] = None
    service_id: Optional[str] = None
    city: Optional[str] = None
    area: Optional[str] = None
    description: Optional[str] = None
