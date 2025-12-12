# app/auth/logic/auth_service.py
from piccolo.apps.user.tables import BaseUser  # ignore if not used
from fastapi import HTTPException, status

from db.tables import Account, Registration
from auth.logic.passwords import hash_password, verify_password
from auth.logic.tokens import create_access_token

async def signup(*, phone: str, password: str, role: str, capacity: str) -> dict:
    existing = await Account.objects().get(Account.phone == phone)
    if existing:
        raise HTTPException(status_code=409, detail="Phone already registered")

    account = Account(phone=phone, password_hash=hash_password(password), is_active=True)
    await account.save()

    reg = Registration(account=account.id, role=role, capacity=capacity)
    await reg.save()

    token = create_access_token(sub=str(account.id))
    return {"account": account, "access_token": token}

async def signin(*, phone: str, password: str) -> str:
    account = await Account.objects().get(Account.phone == phone)
    if not account:
        raise HTTPException(status_code=401, detail="Invalid phone or password")

    if not account.is_active:
        raise HTTPException(status_code=403, detail="Account disabled")

    if not verify_password(password, account.password_hash):
        raise HTTPException(status_code=401, detail="Invalid phone or password")

    return create_access_token(sub=str(account.id))

async def get_me(*, account_id: str) -> dict:
    account = await Account.objects().get(Account.id == account_id)
    if not account:
        raise HTTPException(status_code=401, detail="Account not found")

    reg = await Registration.objects().get(Registration.account == account_id)
    if not reg:
        raise HTTPException(status_code=404, detail="Registration not found")

    return {"accountId": str(account.id), "role": reg.role}