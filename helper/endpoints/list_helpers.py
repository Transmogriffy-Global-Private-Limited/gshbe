from fastapi import APIRouter, Depends, Query, status
from auth.logic.deps import get_current_account_id
from helper.logic.list_helpers import list_helpers
from helper.structs.list_helpers import HelperListOut

router = APIRouter()


@router.get(
    "/list",
    response_model=list[HelperListOut],
    status_code=status.HTTP_200_OK,
    summary="List all helpers",
    description="Returns list of registered helpers with profile details",
)
async def get_helpers(
    city: str | None = Query(default=None),
    area: str | None = Query(default=None),
    min_rating: float | None = Query(default=None),
    account_id: str = Depends(get_current_account_id),
):
    return await list_helpers(
        account_id=account_id,
        city=city,
        area=area,
        min_rating=min_rating,
    )
