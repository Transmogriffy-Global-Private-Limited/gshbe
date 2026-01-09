from helper.tables.helpers import HelperPersonal, HelperInstitutional
from registration.tables.registration import Registration

from helper.structs.dtos import (
    HelperListOut,
    HelperListItemOut,
    HelperPersonalProfileOut,
    HelperInstitutionalProfileOut,
)


async def list_helpers_service():
    # Fetch all helper registrations
    registrations = await Registration.objects().where(
        Registration.role == "helper"
    )

    items = []

    for reg in registrations:
        # PERSONAL HELPERS
        if reg.capacity == "personal":
            profile = await HelperPersonal.objects().where(
                HelperPersonal.registration == reg.id
            ).first()

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
                avg_rating=str(profile.avg_rating),
                rating_count=profile.rating_count,
            )

        # INSTITUTIONAL HELPERS
        else:
            profile = await HelperInstitutional.objects().where(
                HelperInstitutional.code == str(reg.id)
            ).first()

            if not profile:
                continue

            profile_out = HelperInstitutionalProfileOut(
                id=profile.id,
                registration=str(reg.id),
                name=profile.name,
                city=None,
                address=None,
                phone=None,
                avg_rating=None,
                rating_count=0,
            )

        items.append(
            HelperListItemOut(
                registration_id=str(reg.id),
                role="helper",
                capacity=reg.capacity,
                profile_kind=reg.profile_kind,
                profile=profile_out,
            )
        )

    return HelperListOut(items=items)
