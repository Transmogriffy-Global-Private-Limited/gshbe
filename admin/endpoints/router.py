from fastapi import APIRouter, status
from admin.logic.service import (
    admin_signup,
    admin_signin,
    admin_forgot_password,
)
from admin.structs.dtos import (
    AdminSignUpIn,
    AdminSignInIn,
    AdminForgotPasswordIn,
    AdminAuthOut,
)

router = APIRouter(
    prefix="/admin",
    tags=["Admin"],
)


@router.post(
    "/signup",
    response_model=AdminAuthOut,
    status_code=status.HTTP_201_CREATED,
)
async def signup(data: AdminSignUpIn):
    return await admin_signup(data)


@router.post("/signin", response_model=AdminAuthOut)
async def signin(data: AdminSignInIn):
    return await admin_signin(data)


@router.post("/forgot-password")
async def forgot_password(data: AdminForgotPasswordIn):
    return await admin_forgot_password(data)
