from fastapi import APIRouter
from helper.logic.list_helpers import list_helpers
from helper.structs.list_helpers import HelperListResponse

router = APIRouter(prefix="/helpers", tags=["Helpers"])


@router.get("/", response_model=HelperListResponse)
async def get_helpers():
    return await list_helpers()
