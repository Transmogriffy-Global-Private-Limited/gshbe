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
 
    print(f"[DEBUG] Total helper registrations: {len(registrations)}")
 
    for reg in registrations:
        try:
            # ================= PERSONAL =================
            if reg.profile_kind == "helper_personal":
                profile = await HelperPersonal.objects().where(
                    HelperPersonal.registration == reg.id
                ).first()
 
                if not profile:
                    print(f"[WARN] Missing personal profile for {reg.id}")
                    continue
 
                items.append(
                    HelperListItemOut(
                        registration_id=str(reg.id),
                        role="helper",
                        capacity="personal",
                        profile_kind="helper_personal",
                        profile=HelperPersonalProfileOut(
                            id=str(profile.id),
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
                        ),
                    )
                )
 
            # ================= INSTITUTIONAL =================
            elif reg.profile_kind == "helper_institutional":
                profile = await HelperInstitutional.objects().where(
                    HelperInstitutional.registration == reg.id
                ).first()
 
                if not profile:
                    print(f"[WARN] Missing institutional profile for {reg.id}")
                    continue
 
                items.append(
                    HelperListItemOut(
                        registration_id=str(reg.id),
                        role="helper",
                        capacity="institutional",
                        profile_kind="helper_institutional",
                        profile=HelperInstitutionalProfileOut(
                            id=str(profile.id),
                            registration=str(reg.id),
                            institution_name=profile.institution_name,
                            city=profile.city,
                            area=profile.area,
                            phone=profile.phone,
                            avg_rating=str(profile.avg_rating)
                            if profile.avg_rating is not None
                            else None,
                            rating_count=profile.rating_count,
                        ),
                    )
                )
 
            # ================= UNKNOWN =================
            else:
                print(
                    f"[WARN] Unknown profile_kind={reg.profile_kind} "
                    f"for reg={reg.id}"
                )
 
        except Exception as e:
            print(f"[ERROR] Failed processing reg={reg.id}: {e}")
 
    print(f"[DEBUG] Final helper count: {len(items)}")
    return HelperListOut(items=items)