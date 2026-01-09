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
    helpers: list[HelperListItemOut] = []

    # IMPORTANT:
    # registration_id IS THE PRIMARY KEY, NOT A COLUMN
    registrations = await Registration.objects().where(
        Registration.role == "helper"
    )

    for reg in registrations:
        # PERSONAL HELPERS
        if reg.profile_kind == "helper_personal":
            profile = await HelperPersonal.objects().where(
                HelperPersonal.registration == reg.registration_id
            ).first()

            if not profile:
                continue

            helpers.append(
                HelperListItemOut(
                    registration_id=str(reg.registration_id),
                    role=reg.role,
                    capacity=reg.capacity,
                    profile_kind=reg.profile_kind,
                    profile=HelperPersonalProfileOut(
                        id=profile.id,
                        registration=str(profile.registration),
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
                    ),
                )
            )

        # INSTITUTIONAL HELPERS
        elif reg.profile_kind == "helper_institutional":
            profile = await HelperInstitutional.objects().where(
                HelperInstitutional.registration == reg.registration_id
            ).first()

            if not profile:
                continue

            helpers.append(
                HelperListItemOut(
                    registration_id=str(reg.registration_id),
                    role=reg.role,
                    capacity=reg.capacity,
                    profile_kind=reg.profile_kind,
                    profile=HelperInstitutionalProfileOut(
                        id=profile.id,
                        registration=str(profile.registration),
                        institution_name=profile.institution_name,
                        city=profile.city,
                        area=profile.area,
                        phone=profile.phone,
                        avg_rating=str(profile.avg_rating),
                        rating_count=profile.rating_count,
                    ),
                )
            )

    return HelperListOut(items=helpers)
