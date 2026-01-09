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

    items: list[HelperListItemOut] = []

    for reg in registrations:
        if reg.profile_kind == "helper_personal":
            profile = await HelperPersonal.objects().where(
                HelperPersonal.registration == reg.registration_id
            ).first()

            items.append(
                HelperListItemOut(
                    registration_id=reg.registration_id,
                    role=reg.role,
                    capacity=reg.capacity,
                    profile_kind=reg.profile_kind,
                    profile=HelperPersonalProfileOut(**profile.__dict__)
                    if profile else None,
                )
            )

        elif reg.profile_kind == "helper_institutional":
            profile = await HelperInstitutional.objects().where(
                HelperInstitutional.registration == reg.registration_id
            ).first()

            items.append(
                HelperListItemOut(
                    registration_id=reg.registration_id,
                    role=reg.role,
                    capacity=reg.capacity,
                    profile_kind=reg.profile_kind,
                    profile=HelperInstitutionalProfileOut(**profile.__dict__)
                    if profile else None,
                )
            )

    return HelperListOut(items=items)
