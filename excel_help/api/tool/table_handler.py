from fastapi import APIRouter, Depends, status


router = APIRouter()

table_type = {
    "red": 1,
    "douyin": 2
}

@router.post(
    "/test",
    status_code=status.HTTP_200_OK,
    description="Update current user password",
)
async def reset_current_user_password(

) -> str:
    return '{}'