from fastapi import APIRouter
from helper.logic.list_helpers import list_helpers

router = APIRouter()

@router.get("/helper/list_helpers")
async def get_helpers():
    return await list_helpers()
