from pydantic import BaseModel, Field
from auth.structs.enums import Role, Capacity

class SignUpIn(BaseModel):
    phone: str = Field(..., examples=["+919876543210"], description="E.164 preferred")
    password: str = Field(..., min_length=8, examples=["CorrectHorseBatteryStaple"])
    role: Role
    capacity: Capacity

class SignInIn(BaseModel):
    phone: str = Field(..., examples=["+919876543210"])
    password: str = Field(..., min_length=8, examples=["CorrectHorseBatteryStaple"])

class TokenOut(BaseModel):
    access_token: str = Field(..., description="JWT access token")
    token_type: str = Field("bearer")

class SignUpOut(TokenOut):
    kind: str | None = Field(
        None,
        description="Default profile kind for this account (e.g. seeker_personal). None for admin."
    )

class AccountOut(BaseModel):
    id: str
    phone: str
    is_active: bool

class MeOut(BaseModel):
    accountId: str
    role: str
