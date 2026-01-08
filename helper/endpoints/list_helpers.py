from fastapi import APIRouter
from helper.logic.list_helpers import list_helpers
from helper.structs.list_helpers import HelperListResponse

router = APIRouter(
    prefix="/helper",
    tags=["Helper"]
)

@router.get("/list_helpers", response_model=HelperListResponse)
async def get_helpers():
    return await list_helpers()
