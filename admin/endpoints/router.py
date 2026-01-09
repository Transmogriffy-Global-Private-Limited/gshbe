from fastapi import APIRouter, status

from admin.logic.service import admin_signup, admin_signin
from admin.structs.dtos import (
    AdminSignUpIn,
    AdminSignInIn,
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


@router.post(
    "/signin",
    response_model=AdminAuthOut,
)
async def signin(data: AdminSignInIn):
    return await admin_signin(data)
