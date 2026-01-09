from fastapi import APIRouter, status
from helper.logic.list_helpers import list_helpers_service
from helper.structs.dtos import HelperListOut

router = APIRouter()


@router.get(
    "/list_helpers",
    response_model=HelperListOut,
    status_code=status.HTTP_200_OK,
    summary="List available helpers",
)
async def list_helpers_endpoint():
    helpers = await list_helpers_service()
    return {"items": helpers}
