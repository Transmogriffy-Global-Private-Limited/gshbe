# helper/logic/list_helpers.py

from db.tables import Registration, HelperPersonal

async def list_helpers():
    helpers = []

    valid_regs = Registration.select(Registration.id).where(
        Registration.role == "helper",
        Registration.capacity == "personal",
    )

    rows = await HelperPersonal.select(
        HelperPersonal.registration,
        HelperPersonal.name,
        HelperPersonal.age,
        HelperPersonal.faith,
        HelperPersonal.languages,
        HelperPersonal.city,
        HelperPersonal.area,
        HelperPersonal.phone,
        HelperPersonal.years_of_experience,
        HelperPersonal.avg_rating,
        HelperPersonal.rating_count,
    ).where(
        HelperPersonal.registration.is_in(valid_regs)
    )

    for row in rows:
        helpers.append({
            "registration_id": str(row["registration"]),
            "role": "helper",
            "capacity": "personal",
            "profile_kind": "helper_personal",
            "profile": {
                "name": row["name"],
                "age": row["age"],
                "faith": row["faith"],
                "languages": row["languages"],
                "city": row["city"],
                "area": row["area"],
                "phone": row["phone"],
                "years_of_experience": row["years_of_experience"],
                "avg_rating": row["avg_rating"],
                "rating_count": row["rating_count"],
            },
        })

    return helpers
