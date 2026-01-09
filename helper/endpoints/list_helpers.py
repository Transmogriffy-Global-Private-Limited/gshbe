from fastapi import APIRouter
from helper.logic.list_helpers import list_helpers_service
from helper.structs.dtos import HelperListOut

router = APIRouter()

@router.get(
    "/helpers",
    response_model=HelperListOut
)
async def list_helpers_endpoint():
    return await list_helpers_service()
