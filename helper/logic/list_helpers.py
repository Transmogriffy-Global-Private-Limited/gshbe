from db.tables import HelperPersonal, HelperInstitutional, Registration


async def list_helpers():
    helpers = []

    print("👉 Fetching personal helpers...")

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
        HelperPersonal.registration.is_in(
            Registration.select(Registration.id).where(
                Registration.role == "helper",
                Registration.capacity == "personal",
                Registration.is_online == True,
            )
        )
    )

    print("✅ Personal rows:", personal_rows)

    for row in personal_rows:
        helpers.append({
            "registration_id": str(row["registration"]),
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

    print("👉 Fetching institutional helpers...")

    institutional_rows = await HelperInstitutional.select(
        HelperInstitutional.registration,
        HelperInstitutional.name,
        HelperInstitutional.city,
        HelperInstitutional.address,
        HelperInstitutional.phone,
        HelperInstitutional.avg_rating,
        HelperInstitutional.rating_count,
    ).where(
        HelperInstitutional.registration.is_in(
            Registration.select(Registration.id).where(
                Registration.role == "helper",
                Registration.capacity == "institutional",
                Registration.is_online == True,
            )
        )
    )

    print("✅ Institutional rows:", institutional_rows)

    for row in institutional_rows:
        helpers.append({
            "registration_id": str(row["registration"]),
            "type": "institutional",
            "name": row["name"],
            "city": row["city"],
            "address": row["address"],
            "phone": row["phone"],
            "avg_rating": row["avg_rating"],
            "rating_count": row["rating_count"],
        })

    return helpers
