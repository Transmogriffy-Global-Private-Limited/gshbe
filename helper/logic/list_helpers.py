from helper.tables.registration import Registration
from helper.tables.personal import HelperPersonalProfile
from helper.tables.institutional import HelperInstitutionalProfile

from helper.structs.dtos import (
    HelperListOut,
    HelperListItemOut,
    HelperPersonalProfileOut,
    HelperInstitutionalProfileOut,
)


async def list_helpers_service() -> HelperListOut:
    # 1️⃣ Fetch all helper registrations
    registrations = await Registration.objects().where(
        Registration.role == "helper"
    )

    items: list[HelperListItemOut] = []

    for reg in registrations:
        # ==========================
        # PERSONAL HELPER
        # ==========================
        if reg.capacity == "personal":
            profile = (
                await HelperPersonalProfile.objects()
                .where(HelperPersonalProfile.registration == reg.id)
                .first()
            )

            if not profile:
                continue

            profile_out = HelperPersonalProfileOut(
                id=profile.id,
                registration=str(reg.id),
                name=profile.name,
                age=profile.age,
                faith=profile.faith,
                languages=profile.languages,
                city=profile.city,
                area=profile.area,
                phone=profile.phone,
                years_of_experience=profile.years_of_experience,
                avg_rating=str(profile.avg_rating)
                if profile.avg_rating is not None
                else None,
                rating_count=profile.rating_count,
            )

        # ==========================
        # INSTITUTIONAL HELPER
        # ==========================
        elif reg.capacity == "institutional":
            profile = (
                await HelperInstitutionalProfile.objects()
                .where(HelperInstitutionalProfile.registration == reg.id)
                .first()
            )

            if not profile:
                continue

            profile_out = HelperInstitutionalProfileOut(
                id=profile.id,
                registration=str(reg.id),
                name=profile.name,
                city=profile.city,
                address=profile.address,
                phone=profile.phone,
                avg_rating=str(profile.avg_rating)
                if profile.avg_rating is not None
                else None,
                rating_count=profile.rating_count,
            )

        else:
            # Unknown capacity → skip safely
            continue

        # ==========================
        # RESPONSE ITEM
        # ==========================
        items.append(
            HelperListItemOut(
                registration_id=str(reg.id),
                role="helper",
                capacity=reg.capacity,
                profile_kind=f"helper_{reg.capacity}",
                profile=profile_out,
            )
        )

    return HelperListOut(items=items)
