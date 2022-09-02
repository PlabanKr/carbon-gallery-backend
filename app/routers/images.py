from fastapi import APIRouter

router = APIRouter(
    prefix="/image"
)

@router.get("/all")
async def get_all_images():
    return [
        {"username": "Plaban", "email": "plaban.kr.mondal00@gmail.com"},
        {"username": "Plaban", "email": "plaban.kr.mondal00@gmail.com"},
        {"username": "Plaban", "email": "plaban.kr.mondal00@gmail.com"}
    ]


@router.get("/{id}")
async def get_image_by_id(id: int):
    return [
        {"id": id, "username": "Plaban", "email": "plaban.kr.mondal00@gmail.com"}
    ]

    