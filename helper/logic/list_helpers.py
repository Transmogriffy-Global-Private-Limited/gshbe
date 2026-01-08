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
        HelperPersonal.registration.role == "helper",
        HelperPersonal.registration.capacity == "personal",
        HelperPersonal.registration.is_online == True,
    )

    print("✅ Personal rows:", personal_rows)
    print("🔢 Personal count:", len(personal_rows))

    for row in personal_rows:
        print("➡️ Personal helper row:", row)

        helpers.append({
            "registration_id": row["registration"],
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

    print("📦 Helpers after personal:", helpers)

    return helpers
