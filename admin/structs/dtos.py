# from pydantic import BaseModel, Field


# class AdminSignUpIn(BaseModel):
#     name: str = Field(..., example="Admin One")
#     phone_number: str = Field(..., example="9876543210")
#     password: str = Field(..., min_length=6)


# class AdminSignInIn(BaseModel):
#     phone_number: str = Field(..., example="9876543210")
#     password: str


# class AdminAuthOut(BaseModel):
#     access_token: str
#     token_type: str = "bearer"
from pydantic import BaseModel, Field


class AdminSignUpIn(BaseModel):
    name: str = Field(..., example="Admin One")
    phone_number: str = Field(..., example="9876543210")
    password: str = Field(..., min_length=6)


class AdminSignInIn(BaseModel):
    phone_number: str = Field(..., example="9876543210")
    password: str


class AdminAuthOut(BaseModel):
    access_token: str
    token_type: str = "bearer"
