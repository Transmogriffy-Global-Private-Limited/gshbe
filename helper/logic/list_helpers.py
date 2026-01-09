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
    items: list[HelperListItemOut] = []

    # Fetch ALL helper registrations
    registrations = await Registration.objects().where(
        Registration.role == "helper"
    )

    for reg in registrations:
        # ---------------- PERSONAL HELPERS ----------------
        if reg.profile_kind == "helper_personal":
            profile = await HelperPersonal.objects().get(
                HelperPersonal.registration == reg.id
            )

            items.append(
                HelperListItemOut(
                    registration_id=str(reg.id),
                    role=reg.role,
                    capacity=reg.capacity,
                    profile_kind=reg.profile_kind,
                    profile=HelperPersonalProfileOut(
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
                    ),
                )
            )

        # -------------- INSTITUTIONAL HELPERS --------------
        elif reg.profile_kind == "helper_institutional":
            profile = await HelperInstitutional.objects().get(
                HelperInstitutional.registration == reg.id
            )

            items.append(
                HelperListItemOut(
                    registration_id=str(reg.id),
                    role=reg.role,
                    capacity=reg.capacity,
                    profile_kind=reg.profile_kind,
                    profile=HelperInstitutionalProfileOut(
                        id=profile.id,
                        registration=str(reg.id),
                        institution_name=profile.institution_name,
                        city=profile.city,
                        area=profile.area,
                        phone=profile.phone,
                        avg_rating=str(profile.avg_rating),
                        rating_count=profile.rating_count,
                    ),
                )
            )

        # ---------------- UNKNOWN PROFILE ------------------
        else:
            raise ValueError(
                f"Unknown profile_kind '{reg.profile_kind}' "
                f"for registration {reg.id}"
            )

    return HelperListOut(items=items)
