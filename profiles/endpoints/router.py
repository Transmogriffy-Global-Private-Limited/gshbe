# profiles/endpoints/router.py
from fastapi import APIRouter, Depends

from auth.logic.deps import get_current_account_id
from profiles.logic.profile_service import get_my_profile, upsert_my_profile
from profiles.structs.dtos import ProfileOut, ProfileUpsertIn

router = APIRouter()

@router.get("/me", response_model=ProfileOut)
async def me_profile(account_id: str = Depends(get_current_account_id)):
    return await get_my_profile(account_id=account_id)

@router.put("/me", response_model=ProfileOut)
async def upsert_profile(
    payload: ProfileUpsertIn,
    account_id: str = Depends(get_current_account_id),
):
    return await upsert_my_profile(account_id=account_id, payload=payload)
