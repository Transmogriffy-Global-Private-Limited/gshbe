# app/auth/endpoints/router.py
from fastapi import APIRouter, status, Depends
from auth.structs.dtos import SignUpIn, SignInIn, TokenOut, AccountOut
from auth.logic.auth_service import signup, signin
from auth.structs.dtos import MeOut
from auth.logic.deps import get_current_account_id
from auth.logic.auth_service import get_me
router = APIRouter()

@router.post(
    "/signup",
    summary="Sign up with phone + password",
    description="Creates Account + Registration. Returns a JWT access token.",
    response_model=TokenOut,
    status_code=status.HTTP_201_CREATED,
    responses={
        201: {"description": "Created"},
        409: {"description": "Phone already registered"},
    },
)
async def signup_endpoint(payload: SignUpIn):
    result = await signup(
        phone=payload.phone,
        password=payload.password,
        role=payload.role.value,
        capacity=payload.capacity.value,
    )
    return {"access_token": result["access_token"], "token_type": "bearer"}

@router.post(
    "/signin",
    summary="Sign in with phone + password",
    description="Verifies password and returns a JWT access token.",
    response_model=TokenOut,
    responses={
        200: {"description": "OK"},
        401: {"description": "Invalid phone or password"},
        403: {"description": "Account disabled"},
    },
)
async def signin_endpoint(payload: SignInIn):
    token = await signin(phone=payload.phone, password=payload.password)
    return {"access_token": token, "token_type": "bearer"}

@router.get(
    "/me",
    summary="Get current user identity",
    description="Requires a Bearer token. Returns accountId + role.",
    response_model=MeOut,
    responses={
        200: {"description": "OK"},
        401: {"description": "Invalid or expired token"},
        404: {"description": "Registration not found"},
    },
)
async def me_endpoint(account_id: str = Depends(get_current_account_id)):
    return await get_me(account_id=account_id)