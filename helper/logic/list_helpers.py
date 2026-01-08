from db.tables import Registration, HelperPersonal, HelperInstitutional


async def list_helpers():
    helpers = []

    # =========================
    # PERSONAL HELPERS
    # =========================
    personal_reg_ids = (
        Registration.select(Registration.id)
        .where(
            Registration.role == "helper",
            Registration.capacity == "personal",
            Registration.is_online == True,
        )
    )

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
        HelperPersonal.registration.is_in(personal_reg_ids)
    )

    for row in personal_rows:
        helpers.append(
            {
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
            }
        )

    # =========================
    # INSTITUTIONAL HELPERS
    # =========================
    institutional_reg_ids = (
        Registration.select(Registration.id)
        .where(
            Registration.role == "helper",
            Registration.capacity == "institutional",
            Registration.is_online == True,
        )
    )

    institutional_rows = await HelperInstitutional.select(
        HelperInstitutional.registration,
        HelperInstitutional.name,
        HelperInstitutional.city,
        HelperInstitutional.address,
        HelperInstitutional.phone,
        HelperInstitutional.avg_rating,
        HelperInstitutional.rating_count,
    ).where(
        HelperInstitutional.registration.is_in(institutional_reg_ids)
    )

    for row in institutional_rows:
        helpers.append(
            {
                "registration_id": str(row["registration"]),
                "role": "helper",
                "capacity": "institutional",
                "profile_kind": "helper_institutional",
                "profile": {
                    "name": row["name"],
                    "city": row["city"],
                    "address": row["address"],
                    "phone": row["phone"],
                    "avg_rating": row["avg_rating"],
                    "rating_count": row["rating_count"],
                },
            }
        )

    return helpers
