from decimal import Decimal
from helper.tables.registration import Registration
from helper.tables.personal import HelperPersonal


def str_or_zero(val):
    if val is None:
        return "0"
    if isinstance(val, Decimal):
        return str(val)
    return str(val)


async def list_helpers_service():
    helpers = []

    valid_regs = (
        Registration.select(Registration.id)
        .where(
            Registration.role == "helper",
            Registration.capacity == "personal",
        )
    )

    rows = await HelperPersonal.select(
        HelperPersonal.id,
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
        helpers.append(
            {
                "registration_id": str(row["registration"]),
                "role": "helper",
                "capacity": "personal",
                "profile_kind": "helper_personal",
                "profile": {
                    "id": row["id"],
                    "registration": str(row["registration"]),
                    "name": row["name"],
                    "age": row["age"],
                    "faith": row["faith"],
                    "languages": row["languages"],
                    "city": row["city"],
                    "area": row["area"],
                    "phone": row["phone"] or "",
                    "years_of_experience": row["years_of_experience"],
                    "avg_rating": str_or_zero(row["avg_rating"]),  # ✅ FIX
                    "rating_count": row["rating_count"],
                },
            }
        )

    return helpers
