from fastapi import HTTPException, status
from admin.tables.admin import Admin
from admin.structs.dtos import (
    AdminSignUpIn,
    AdminSignInIn,
    AdminAuthOut,
    AdminForgotPasswordIn,
)
from auth.logic.security import (
    hash_password,
    verify_password,
    create_access_token,
)


async def admin_signup(data: AdminSignUpIn) -> AdminAuthOut:
    if await Admin.objects().where(Admin.email == data.email).first():
        raise HTTPException(status_code=400, detail="Admin already exists")

    admin = Admin(
        email=data.email,
        password_hash=hash_password(data.password),
    )
    await admin.save()

    token = create_access_token(
        {"sub": str(admin.id), "role": "admin"}
    )
    return AdminAuthOut(access_token=token)


async def admin_signin(data: AdminSignInIn) -> AdminAuthOut:
    admin = await Admin.objects().where(Admin.email == data.email).first()
    if not admin or not verify_password(data.password, admin.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )

    token = create_access_token(
        {"sub": str(admin.id), "role": "admin"}
    )
    return AdminAuthOut(access_token=token)


async def admin_forgot_password(data: AdminForgotPasswordIn):
    admin = await Admin.objects().where(Admin.email == data.email).first()
    if not admin:
        raise HTTPException(status_code=404, detail="Admin not found")

    # email sending will be added later
    return {"message": "Password reset link sent"}
