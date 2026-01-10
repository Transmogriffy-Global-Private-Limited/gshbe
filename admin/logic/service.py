# from fastapi import HTTPException, status

# from admin.tables.admin import Admin
# from admin.structs.dtos import (
#     AdminSignUpIn,
#     AdminSignInIn,
#     AdminAuthOut,
# )
# from auth.logic.security import (
#     hash_password,
#     verify_password,
#     create_access_token,
# )


# async def admin_signup(data: AdminSignUpIn) -> AdminAuthOut:
#     existing_admin = await Admin.objects().where(
#         Admin.phone_number == data.phone_number
#     ).first()

#     if existing_admin:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="Admin with this phone number already exists",
#         )

#     admin = Admin(
#         name=data.name,
#         phone_number=data.phone_number,
#         password_hash=hash_password(data.password),
#     )
#     await admin.save()

#     token = create_access_token(
#         {"sub": str(admin.id), "role": "admin"}
#     )

#     return AdminAuthOut(access_token=token)


# async def admin_signin(data: AdminSignInIn) -> AdminAuthOut:
#     admin = await Admin.objects().where(
#         Admin.phone_number == data.phone_number
#     ).first()

#     if not admin or not verify_password(data.password, admin.password_hash):
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid phone number or password",
#         )

#     token = create_access_token(
#         {"sub": str(admin.id), "role": "admin"}
#     )

#     return AdminAuthOut(access_token=token)
from fastapi import HTTPException, status

from admin.tables.admin import Admin
from admin.structs.dtos import (
    AdminSignUpIn,
    AdminSignInIn,
    AdminAuthOut,
)
from auth.logic.security import (
    hash_password,
    verify_password,
    create_access_token,
)


async def admin_signup(data: AdminSignUpIn) -> AdminAuthOut:
    existing_admin = await Admin.objects().where(
        Admin.phone_number == data.phone_number
    ).first()

    if existing_admin:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Admin with this phone number already exists",
        )

    admin = Admin(
        name=data.name,
        phone_number=data.phone_number,
        password_hash=hash_password(data.password),
    )
    await admin.save()

    token = create_access_token(
        {"sub": str(admin.id), "role": "admin"}
    )

    return AdminAuthOut(access_token=token)


async def admin_signin(data: AdminSignInIn) -> AdminAuthOut:
    admin = await Admin.objects().where(
        Admin.phone_number == data.phone_number
    ).first()

    if not admin or not verify_password(data.password, admin.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid phone number or password",
        )

    token = create_access_token(
        {"sub": str(admin.id), "role": "admin"}
    )

    return AdminAuthOut(access_token=token)
