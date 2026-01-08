# helper/logic/list_helpers.py

from db.tables import Registration, HelperPersonal, HelperInstitutional


async def list_helpers():
    # -------------------------------
    # PERSONAL HELPERS
    # -------------------------------
    print("👉 Fetching personal helpers...")

    valid_regs = (
        Registration.select(Registration.id)
        .where(
            Registration.role == "helper",
            Registration.capacity == "personal",
        )
    )

    personal_rows = await HelperPersonal.select(
        HelperPersonal.registration,
        HelperPersonal.name,
        HelperPersonal.age,
        HelperPersonal.city,
        HelperPersonal.area,
        HelperPersonal.phone,
        HelperPersonal.years_of_experience,
        HelperPersonal.avg_rating,
        HelperPersonal.rating_count,
    ).where(
        HelperPersonal.registration.is_in(valid_regs)
    )

    print(f"✅ Personal rows: {personal_rows}")

    # -------------------------------
    # INSTITUTIONAL HELPERS
    # -------------------------------
    print("👉 Fetching institutional helpers...")

    valid_regs_inst = (
        Registration.select(Registration.id)
        .where(
            Registration.role == "helper",
            Registration.capacity == "institutional",
        )
    )

    institutional_rows = await HelperInstitutional.select(
        HelperInstitutional.registration,
        HelperInstitutional.name,
        HelperInstitutional.city,
        HelperInstitutional.phone,
        HelperInstitutional.avg_rating,
        HelperInstitutional.rating_count,
    ).where(
        HelperInstitutional.registration.is_in(valid_regs_inst)
    )

    print(f"✅ Institutional rows: {institutional_rows}")

    return {
        "personal": personal_rows,
        "institutional": institutional_rows,
    }
