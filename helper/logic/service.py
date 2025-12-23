from fastapi import HTTPException, status

from db.tables import (
    Registration,
    HelperPreference,
    HelperPreferredService,
    HelperExperience,
    Service,
)


# ----------------------------
# Internal helpers
# ----------------------------

async def _get_registration_by_account_id(account_id: str) -> Registration:
    reg = await Registration.objects().where(Registration.account == account_id).first()
    if not reg:
        raise HTTPException(status_code=404, detail="Registration not found")
    return reg


def _ensure_helper(reg: Registration) -> None:
    if reg.role not in ("helper", "both"):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only helpers can access this resource",
        )


async def _validate_service_ids(service_ids: list[str]) -> None:
    if not service_ids:
        return

    rows = await Service.objects().where(Service.id.is_in(service_ids)).columns(Service.id)
    found = {str(r["id"]) for r in rows}
    missing = [sid for sid in service_ids if sid not in found]
    if missing:
        raise HTTPException(status_code=400, detail=f"Invalid service_ids: {missing}")


def _validate_years(year_from: int | None, year_to: int | None) -> None:
    if year_from is not None and year_to is not None and year_from > year_to:
        raise HTTPException(status_code=400, detail="year_from cannot be greater than year_to")


# ----------------------------
# Public read (ANYONE)
# ----------------------------

async def get_preference_by_registration_id(*, registration_id: str) -> dict:
    pref = await HelperPreference.objects().where(
        HelperPreference.registration == registration_id
    ).first()

    if not pref:
        return {
            "registration_id": str(registration_id),
            "city": None,
            "area": None,
            "job_type": None,
            "preferred_service_ids": [],
        }

    pref_services = await HelperPreferredService.objects().where(
        HelperPreferredService.registration == registration_id
    ).columns(HelperPreferredService.service)

    return {
        "registration_id": str(registration_id),
        "city": pref.city,
        "area": pref.area,
        "job_type": pref.job_type,
        "preferred_service_ids": [str(r["service"]) for r in pref_services],
    }


async def list_experience_by_registration_id(*, registration_id: str) -> list[dict]:
    rows = await HelperExperience.objects().where(
        HelperExperience.registration == registration_id
    )

    return [
        {
            "id": str(r.id),
            "registration_id": str(registration_id),
            "year_from": r.year_from,
            "year_to": r.year_to,
            "service_id": str(r.service) if r.service else None,
            "city": r.city,
            "area": r.area,
            "description": r.description,
        }
        for r in rows
    ]


# ----------------------------
# Owner-only
# ----------------------------

async def get_my_preference(*, account_id: str) -> dict:
    reg = await _get_registration_by_account_id(account_id)
    _ensure_helper(reg)
    return await get_preference_by_registration_id(registration_id=str(reg.id))


async def upsert_my_preference(*, account_id: str, payload: dict) -> dict:
    reg = await _get_registration_by_account_id(account_id)
    _ensure_helper(reg)

    preferred_service_ids = payload.get("preferred_service_ids", [])
    await _validate_service_ids(preferred_service_ids)

    existing = await HelperPreference.objects().where(
        HelperPreference.registration == reg.id
    ).first()

    data = {
        "city": payload.get("city"),
        "area": payload.get("area"),
        "job_type": payload.get("job_type"),
    }

    if existing:
        for k, v in data.items():
            setattr(existing, k, v)
        await existing.save()
    else:
        row = HelperPreference(registration=reg.id, **data)
        await row.save()

    await HelperPreferredService.delete().where(
        HelperPreferredService.registration == reg.id
    )

    if preferred_service_ids:
        await HelperPreferredService.insert(
            *[
                HelperPreferredService(registration=reg.id, service=sid)
                for sid in preferred_service_ids
            ]
        )

    return await get_my_preference(account_id=account_id)


async def list_my_experience(*, account_id: str) -> list[dict]:
    reg = await _get_registration_by_account_id(account_id)
    _ensure_helper(reg)
    return await list_experience_by_registration_id(registration_id=str(reg.id))


async def create_my_experience(*, account_id: str, payload: dict) -> dict:
    reg = await _get_registration_by_account_id(account_id)
    _ensure_helper(reg)

    _validate_years(payload.get("year_from"), payload.get("year_to"))

    service_id = payload.get("service_id")
    if service_id:
        await _validate_service_ids([service_id])

    row = HelperExperience(registration=reg.id, **payload)
    await row.save()

    return {
        "id": str(row.id),
        "registration_id": str(reg.id),
        "year_from": row.year_from,
        "year_to": row.year_to,
        "service_id": str(row.service) if row.service else None,
        "city": row.city,
        "area": row.area,
        "description": row.description,
    }


async def update_my_experience(*, account_id: str, experience_id: str, payload: dict) -> dict:
    reg = await _get_registration_by_account_id(account_id)
    _ensure_helper(reg)

    row = await HelperExperience.objects().where(
        HelperExperience.id == experience_id
    ).first()

    if not row or str(row.registration) != str(reg.id):
        raise HTTPException(status_code=404, detail="Experience not found")

    year_from = payload.get("year_from", row.year_from)
    year_to = payload.get("year_to", row.year_to)
    _validate_years(year_from, year_to)

    if "service_id" in payload and payload["service_id"]:
        await _validate_service_ids([payload["service_id"]])

    for k, v in payload.items():
        setattr(row, k, v)

    await row.save()

    return {
        "id": str(row.id),
        "registration_id": str(reg.id),
        "year_from": row.year_from,
        "year_to": row.year_to,
        "service_id": str(row.service) if row.service else None,
        "city": row.city,
        "area": row.area,
        "description": row.description,
    }


async def delete_my_experience(*, account_id: str, experience_id: str) -> dict:
    reg = await _get_registration_by_account_id(account_id)
    _ensure_helper(reg)

    row = await HelperExperience.objects().where(
        HelperExperience.id == experience_id
    ).first()

    if not row or str(row.registration) != str(reg.id):
        raise HTTPException(status_code=404, detail="Experience not found")

    await HelperExperience.delete().where(HelperExperience.id == experience_id)
    return {"deleted": True}
