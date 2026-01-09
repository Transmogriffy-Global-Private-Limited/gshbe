from helper.tables.registration import Registration
from helper.tables.helper_personal_profile import HelperPersonalProfile


async def list_helpers_service():
    """
    Returns all helpers with their personal profile
    Works correctly for:
    - Bruno
    - Swagger
    - PostgreSQL
    """

    # 1. Fetch only helper registrations
    registrations = await Registration.objects().where(
        Registration.role == "helper"
    )

    response = []

    for reg in registrations:
        profile_data = None

        # 2. Fetch personal profile ONLY if profile_kind is helper_personal
        if reg.profile_kind == "helper_personal":
            profile = await HelperPersonalProfile.objects().where(
                HelperPersonalProfile.registration == reg.registration_id
            ).first()

            if profile:
                profile_data = {
                    "id": profile.id,
                    "registration": str(profile.registration),
                    "name": profile.name,
                    "age": profile.age,
                    "faith": profile.faith,
                    "languages": profile.languages,
                    "city": profile.city,
                    "area": profile.area,
                    "phone": profile.phone,
                    "years_of_experience": profile.years_of_experience,
                    "avg_rating": str(profile.avg_rating),
                    "rating_count": profile.rating_count,
                }

        # 3. Final response object (THIS MATCHES YOUR BRUNO OUTPUT)
        response.append({
            "registration_id": str(reg.registration_id),
            "role": reg.role,
            "capacity": reg.capacity,
            "profile_kind": reg.profile_kind,
            "profile": profile_data,
        })

    return response
