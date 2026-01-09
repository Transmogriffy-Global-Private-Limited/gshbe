from helper.tables.registration import Registration
from helper.tables.helpers import Helper
from helper.tables.personal import HelperPersonal
from helper.tables.institutional import HelperInstitutional


async def list_helpers_service():
    # 1️⃣ Get all helper registrations
    registrations = await Registration.objects().where(
        Registration.role == "helper"
    )

    if not registrations:
        return []

    registration_ids = [r["registration_id"] for r in registrations]

    # 2️⃣ Load helpers
    helpers = await Helper.objects().where(
        Helper.is_active == 1
    )

    # 3️⃣ Load personal + institutional profiles
    personals = await HelperPersonal.objects().where(
        HelperPersonal.registration.is_in(registration_ids)
    )

    institutionals = await HelperInstitutional.objects().where(
        HelperInstitutional.code.is_not_null()
    )

    personal_map = {p["registration"]: p for p in personals}
    institutional_map = {i["id"]: i for i in institutionals}

    response = []

    for reg in registrations:
        reg_id = reg["registration_id"]

        if reg["capacity"] == "personal":
            profile = personal_map.get(reg_id)
            if not profile:
                continue

            response.append({
                "registration_id": str(reg_id),
                "role": "helper",
                "capacity": "personal",
                "profile_kind": "helper_personal",
                "profile": {
                    "registration": str(profile["registration"]),
                    "name": profile["name"],
                    "age": profile["age"],
                    "faith": profile["faith"],
                    "languages": profile["languages"],
                    "city": profile["city"],
                    "area": profile["area"],
                    "phone": profile["phone"],
                    "years_of_experience": profile["years_of_experience"],
                    "avg_rating": profile["avg_rating"],
                    "rating_count": profile["rating_count"],
                },
            })

        elif reg["capacity"] == "institutional":
            profile = institutional_map.get(reg_id)
            if not profile:
                continue

            response.append({
                "registration_id": str(reg_id),
                "role": "helper",
                "capacity": "institutional",
                "profile_kind": "helper_institutional",
                "profile": {
                    "registration": str(reg_id),
                    "name": profile["name"],
                    "city": None,
                    "address": None,
                    "phone": None,
                    "avg_rating": "0",
                    "rating_count": 0,
                },
            })

    return response
