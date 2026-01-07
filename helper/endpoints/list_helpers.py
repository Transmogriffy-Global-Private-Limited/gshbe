from fastapi import APIRouter
from helper.logic.list_helpers import list_helpers

router = APIRouter(prefix="/helpers", tags=["Helpers"])


@router.get("/")
async def get_helpers():
    return await list_helpers()
