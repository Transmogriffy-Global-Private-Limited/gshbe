from db.tables import (
    Registration,
    HelperPersonal,
    HelperInstitutional,
)


async def list_helpers():
    helpers = []

    # -------------------------
    # PERSONAL HELPERS
    # -------------------------
    personal_rows = await HelperPersonal.select(
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
        HelperPersonal.registration.role == "helper",
        HelperPersonal.registration.capacity == "personal",
        HelperPersonal.registration.is_online == True,
    )

    for row in personal_rows:
        helpers.append({
            "registration_id": row["registration"],  # UUID (no str())
            "type": "personal",
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
        })

    # -------------------------
    # INSTITUTIONAL HELPERS
    # -------------------------
    institutional_rows = await HelperInstitutional.select(
        HelperInstitutional.registration,
        HelperInstitutional.name,
        HelperInstitutional.city,
        HelperInstitutional.address,
        HelperInstitutional.phone,
        HelperInstitutional.avg_rating,
        HelperInstitutional.rating_count,
    ).where(
        HelperInstitutional.registration.role == "helper",
        HelperInstitutional.registration.capacity == "institutional",
        HelperInstitutional.registration.is_online == True,
    )

    for row in institutional_rows:
        helpers.append({
            "registration_id": row["registration"],  # UUID
            "type": "institutional",
            "name": row["name"],
            "city": row["city"],
            "address": row["address"],
            "phone": row["phone"],
            "avg_rating": row["avg_rating"],
            "rating_count": row["rating_count"],
        })

    return helpers
