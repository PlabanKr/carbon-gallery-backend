from fastapi import APIRouter

router = APIRouter(
    prefix="/user"
)

@router.get("/all")
async def get_all_users():
    return [
        {"username": "Plaban", "email": "plaban.kr.mondal00@gmail.com"},
        {"username": "Plaban", "email": "plaban.kr.mondal00@gmail.com"},
        {"username": "Plaban", "email": "plaban.kr.mondal00@gmail.com"}
    ]


@router.get("/{id}")
async def get_user_by_id(id: int):
    return [
        {"id": id, "username": "Plaban", "email": "plaban.kr.mondal00@gmail.com"}
    ]

    