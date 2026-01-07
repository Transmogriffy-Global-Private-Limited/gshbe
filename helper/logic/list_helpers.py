from fastapi import HTTPException, status
from db.tables import (
    Account,
    Registration,
    HelperPreference,
    HelperPreferredService,
)


async def list_helpers() -> list[dict]:
    """
    Returns all active helpers (role = helper | both).
    """

    regs = await Registration.objects().where(
        Registration.role.is_in(["helper", "both"])
    )

    results: list[dict] = []

    for reg in regs:
        account = await Account.objects().where(
            Account.id == reg.account,
            Account.is_active == True,
        ).first()

        if not account:
            continue

        pref = await HelperPreference.objects().where(
            HelperPreference.registration == reg.id
        ).first()

        services = await HelperPreferredService.objects().where(
            HelperPreferredService.registration == reg.id
        ).columns(HelperPreferredService.service)

        results.append({
            "registration_id": str(reg.id),
            "account_id": str(reg.account),
            "city": pref.city if pref else None,
            "area": pref.area if pref else None,
            "job_type": pref.job_type if pref else None,
            "preferred_service_ids": [str(s["service"]) for s in services],
        })

    return results
