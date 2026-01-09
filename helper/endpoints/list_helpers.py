from fastapi import APIRouter
from helper.logic.list_helpers import list_helpers_service
from helper.structs.dtos import HelperListOut

router = APIRouter()


@router.get(
    "/list_helpers",
    response_model=HelperListOut,
    summary="List available personal helpers",
    description="Returns all personal helpers with profile details",
)
async def list_helpers_endpoint():
    items = await list_helpers_service()
    return {"items": items}
