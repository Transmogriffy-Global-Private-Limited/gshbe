from decimal import Decimal

from helper.tables.registration import Registration
from helper.tables.personal import HelperPersonal
from helper.tables.institutional import HelperInstitutional


def str_or_zero(val):
    if val is None:
        return "0"
    if isinstance(val, Decimal):
        return str(val)
    return str(val)


async def list_helpers_service():
    helpers = []

    # ======================================================
    # PERSONAL HELPERS
    # ======================================================
    personal_rows = await (
        Registration
        .select(
            Registration.registration_id,
            Registration.role,
            Registration.capacity,
            Registration.profile_kind,

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
        )
        .join(
            HelperPersonal,
            on=(HelperPersonal.registration == Registration.registration_id),
        )
        .where(
            Registration.role == "helper",
            Registration.capacity == "personal",
        )
    )

    for r in personal_rows:
        helpers.append(
            {
                "registration_id": str(r["registration_id"]),
                "role": r["role"],
                "capacity": r["capacity"],
                "profile_kind": r["profile_kind"],
                "profile": {
                    "id": r["id"],
                    "registration": str(r["registration"]),
                    "name": r["name"],
                    "age": r["age"],
                    "faith": r["faith"],
                    "languages": r["languages"],
                    "city": r["city"],
                    "area": r["area"],
                    "phone": r["phone"] or "",
                    "years_of_experience": r["years_of_experience"],
                    "avg_rating": str_or_zero(r["avg_rating"]),
                    "rating_count": r["rating_count"],
                },
            }
        )

    # ======================================================
    # INSTITUTIONAL HELPERS
    # ======================================================
    institutional_rows = await (
        Registration
        .select(
            Registration.registration_id,
            Registration.role,
            Registration.capacity,
            Registration.profile_kind,

            HelperInstitutional.id,
            HelperInstitutional.registration,
            HelperInstitutional.name,
            HelperInstitutional.city,
            HelperInstitutional.address,
            HelperInstitutional.phone,
            HelperInstitutional.avg_rating,
            HelperInstitutional.rating_count,
        )
        .join(
            HelperInstitutional,
            on=(HelperInstitutional.registration == Registration.registration_id),
        )
        .where(
            Registration.role == "helper",
            Registration.capacity == "institutional",
        )
    )

    for r in institutional_rows:
        helpers.append(
            {
                "registration_id": str(r["registration_id"]),
                "role": r["role"],
                "capacity": r["capacity"],
                "profile_kind": r["profile_kind"],
                "profile": {
                    "id": r["id"],
                    "registration": str(r["registration"]),
                    "name": r["name"],
                    "city": r["city"],
                    "address": r["address"],
                    "phone": r["phone"] or "",
                    "avg_rating": str_or_zero(r["avg_rating"]),
                    "rating_count": r["rating_count"],
                },
            }
        )

    return helpers
