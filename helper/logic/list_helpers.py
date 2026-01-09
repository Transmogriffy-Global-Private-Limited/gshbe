from helper.tables.helpers import Registration
from helper.tables.personal import HelperPersonal
from helper.tables.institutional import HelperInstitutional

from helper.structs.dtos import (
    HelperListOut,
    HelperListItemOut,
    HelperPersonalProfileOut,
    HelperInstitutionalProfileOut,
)


async def list_helpers_service() -> HelperListOut:
    registrations = await Registration.objects().where(
        Registration.role == "helper"   # ✅ ONLY real columns
    )

    items = []

    for reg in registrations:

        # ---------- PERSONAL ----------
        if reg.capacity == "personal":
            profile = await HelperPersonal.objects().where(
                HelperPersonal.registration == reg.id   # ✅ FIXED
            ).first()

            if not profile:
                continue

            profile_out = HelperPersonalProfileOut(
                id=str(profile.id),
                registration=str(reg.id),               # ✅ FIXED
                name=profile.name,
                age=profile.age,
                faith=profile.faith,
                languages=profile.languages,
                city=profile.city,
                area=profile.area,
                phone=profile.phone,
                years_of_experience=profile.years_of_experience,
                avg_rating=str(profile.avg_rating) if profile.avg_rating else None,
                rating_count=profile.rating_count,
            )

        # ---------- INSTITUTIONAL ----------
        else:
            profile = await HelperInstitutional.objects().where(
                HelperInstitutional.code == str(reg.id) # ✅ FIXED
            ).first()

            if not profile:
                continue

            profile_out = HelperInstitutionalProfileOut(
                id=str(profile.id),
                registration=str(reg.id),               # ✅ FIXED
                name=profile.name,
                city=None,
                address=None,
                phone=None,
                avg_rating=None,
                rating_count=0,
            )

        items.append(
            HelperListItemOut(
                registration_id=str(reg.id),             # ✅ OUTPUT FIELD OK
                role="helper",
                capacity=reg.capacity,
                profile_kind=reg.profile_kind,
                profile=profile_out,
            )
        )

    return HelperListOut(items=items)
