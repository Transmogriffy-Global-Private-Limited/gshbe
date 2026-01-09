from helper.tables.registration import Registration
from helper.tables.personal import HelperPersonal
from helper.tables.institutional import HelperInstitutional


async def list_helpers_service():
    helpers = []

    registrations = await Registration.objects().where(
        Registration.role == "helper"
    )

    reg_map = {str(r.registration_id): r for r in registrations}

    # ---------------- PERSONAL ----------------
    personal_rows = await HelperPersonal.objects()

    for p in personal_rows:
        reg = reg_map.get(str(p.registration))
        if not reg or reg.capacity != "personal":
            continue

        helpers.append({
            "registration_id": str(p.registration),
            "role": reg.role,
            "capacity": reg.capacity,
            "profile_kind": reg.profile_kind,
            "profile": {
                "registration": str(p.registration),
                "name": p.name,
                "age": p.age,
                "faith": p.faith,
                "languages": p.languages,
                "city": p.city,
                "area": p.area,
                "phone": p.phone,
                "years_of_experience": p.years_of_experience,
                "avg_rating": p.avg_rating,
                "rating_count": p.rating_count,
            },
        })

    # ---------------- INSTITUTIONAL ----------------
    institutional_rows = await HelperInstitutional.objects()

    for i in institutional_rows:
        reg = reg_map.get(str(i.registration))
        if not reg or reg.capacity != "institutional":
            continue

        helpers.append({
            "registration_id": str(i.registration),
            "role": reg.role,
            "capacity": reg.capacity,
            "profile_kind": reg.profile_kind,
            "profile": {
                "registration": str(i.registration),
                "name": i.name,
                "city": i.city,
                "address": i.address,
                "phone": i.phone,
                "avg_rating": i.avg_rating,
                "rating_count": i.rating_count,
            },
        })

    return helpers
