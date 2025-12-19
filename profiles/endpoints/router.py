# profiles/endpoints/router.py
from fastapi import APIRouter, Depends, Body

from auth.logic.deps import get_current_account_id
from profiles.logic.profile_service import get_my_profile, upsert_my_profile
from profiles.structs.dtos import ProfileOut, ProfileUpsertIn

router = APIRouter()

@router.get("/me", response_model=ProfileOut, summary="Get My Profile")
async def me_profile(account_id: str = Depends(get_current_account_id)):
    return await get_my_profile(account_id=account_id)


@router.put(
    "/me",
    response_model=ProfileOut,
    summary="Upsert Profile",
    description=(
        "Send exactly one payload shape. Choose by setting `kind`.\n\n"
        "- `seeker_personal` => {name, city, area}\n"
        "- `seeker_institutional` => {name, city, area, institution_type?, phone?}\n"
        "- `helper_personal` => {name, city, area, age?, faith?, languages?, phone?, years_of_experience?}\n"
        "- `helper_institutional` => {name, city, address, phone?}\n"
    ),
)
async def upsert_profile(
    payload: ProfileUpsertIn = Body(
        ...,
        openapi_examples={
            "seeker_personal": {
                "summary": "Seeker • Personal",
                "value": {
                    "kind": "seeker_personal",
                    "name": "Akash",
                    "city": "Kolkata",
                    "area": "Salt Lake",
                },
            },
            "seeker_institutional": {
                "summary": "Seeker • Institutional",
                "value": {
                    "kind": "seeker_institutional",
                    "name": "ABC Hospital",
                    "city": "Kolkata",
                    "area": "Park Street",
                    "institution_type": "Hospital",
                    "phone": "9999999999",
                },
            },
            "helper_personal": {
                "summary": "Helper • Personal",
                "value": {
                    "kind": "helper_personal",
                    "name": "Akash",
                    "city": "Kolkata",
                    "area": "Salt Lake",
                    "languages": "English,Hindi,Bengali",
                    "years_of_experience": 3,
                },
            },
            "helper_institutional": {
                "summary": "Helper • Institutional",
                "value": {
                    "kind": "helper_institutional",
                    "name": "Care Agency X",
                    "city": "Mumbai",
                    "address": "Andheri East",
                    "phone": "8888888888",
                },
            },
        },
    ),
    account_id: str = Depends(get_current_account_id),
):
    return await upsert_my_profile(account_id=account_id, payload=payload)
