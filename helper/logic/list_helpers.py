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

    registrations = await Registration.objects().where(
        Registration.role == "helper"
    )

    for reg in registrations:
        try:
            # ---------------- PERSONAL ----------------
            if reg.profile_kind == "helper_personal":
                profile = await HelperPersonal.objects().where(
                    HelperPersonal.registration == reg.id
                ).first()

                if not profile:
                    print(
                        f"[WARN] Missing personal profile for registration {reg.id}"
                    )
                    continue

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

            # ---------------- INSTITUTIONAL ----------------
            elif reg.profile_kind == "helper_institutional":
                profile = await HelperInstitutional.objects().where(
                    HelperInstitutional.registration == reg.id
                ).first()

                if not profile:
                    print(
                        f"[WARN] Missing institutional profile for registration {reg.id}"
                    )
                    continue

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

            # ---------------- UNKNOWN ----------------
            else:
                print(
                    f"[WARN] Unknown profile_kind {reg.profile_kind} "
                    f"for registration {reg.id}"
                )

        except Exception as e:
            print(
                f"[ERROR] Failed processing registration {reg.id}: {e}"
            )

    return HelperListOut(items=items)
