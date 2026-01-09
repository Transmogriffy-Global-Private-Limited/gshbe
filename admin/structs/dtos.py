from pydantic import BaseModel, EmailStr


class AdminSignUpIn(BaseModel):
    email: EmailStr
    password: str


class AdminSignInIn(BaseModel):
    email: EmailStr
    password: str


class AdminAuthOut(BaseModel):
    access_token: str
    token_type: str = "bearer"


class AdminForgotPasswordIn(BaseModel):
    email: EmailStr
