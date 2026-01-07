from fastapi import APIRouter, status
from helper.logic.list_helpers import list_helpers
from helper.structs.list_helpers import HelperListOut

router = APIRouter()


@router.get(
    "/list",
    response_model=list[HelperListOut],
    status_code=status.HTTP_200_OK,
    summary="List all helpers",
    description=(
        "Public endpoint.\n\n"
        "Returns all registered helpers with active accounts.\n\n"
        "Notes:\n"
        "- role = helper or both\n"
        "- This does NOT mean currently online\n"
        "- JWT is NOT required\n"
    ),
)
async def get_helpers():
    return await list_helpers()
