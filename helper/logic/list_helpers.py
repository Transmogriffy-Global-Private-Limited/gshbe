from fastapi import HTTPException, status
from db.tables import Registration, HelperProfile


async def _ensure_logged_in(account_id: str) -> None:
    reg = await Registration.objects().where(
        Registration.account == account_id
    ).first()

    if not reg:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid account",
        )


async def list_helpers(
    *,
    account_id: str,
    city: str | None,
    area: str | None,
    min_rating: float | None,
) -> list[dict]:

    await _ensure_logged_in(account_id)

    query = HelperProfile.objects()

    if city:
        query = query.where(HelperProfile.city == city)

    if area:
        query = query.where(HelperProfile.area == area)

    if min_rating is not None:
        query = query.where(HelperProfile.avg_rating >= min_rating)

    rows = await query

    return [
        {
            "registration_id": str(r.registration),
            "name": r.name,
            "age": r.age,
            "faith": r.faith,
            "languages": r.languages,
            "city": r.city,
            "area": r.area,
            "phone": r.phone,
            "years_of_experience": r.years_of_experience,
            "avg_rating": float(r.avg_rating) if r.avg_rating is not None else None,
            "rating_count": r.rating_count,
        }
        for r in rows
    ]
