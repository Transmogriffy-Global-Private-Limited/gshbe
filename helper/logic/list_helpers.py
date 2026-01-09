from helper.tables.registration import Registration
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
        Registration.role == "helper"
    )

    items = []

    for reg in registrations:
        if reg.capacity == "personal":
            profile = await HelperPersonal.objects().where(
                HelperPersonal.registration == reg.registration_id
            ).first()

            if not profile:
                continue

            profile_out = HelperPersonalProfileOut(
                id=profile.id,
                registration=reg.registration_id,
                name=profile.name,
                age=profile.age,
                faith=profile.faith,
                languages=profile.languages,
                city=profile.city,
                area=profile.area,
                phone=profile.phone,
                years_of_experience=profile.years_of_experience,
                avg_rating=str(profile.avg_rating),
                rating_count=profile.rating_count,
            )

        else:
            profile = await HelperInstitutional.objects().where(
                HelperInstitutional.code == reg.registration_id
            ).first()

            if not profile:
                continue

            profile_out = HelperInstitutionalProfileOut(
                id=profile.id,
                registration=reg.registration_id,
                name=profile.name,
                city=None,
                address=None,
                phone=None,
                avg_rating=None,
                rating_count=0,
            )

        items.append(
            HelperListItemOut(
                registration_id=reg.registration_id,
                role="helper",
                capacity=reg.capacity,
                profile_kind=f"helper_{reg.capacity}",
                profile=profile_out,
            )
        )

    return HelperListOut(items=items)
