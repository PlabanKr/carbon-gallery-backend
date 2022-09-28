from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db.main import SessionLocal
from ..db import crud, schemas

# Database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter(
    prefix="/image"
)


# Get Routes
@router.get("/all", response_model=list[schemas.Image])
async def get_all_images(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    images = crud.get_images(db, skip=skip, limit=limit)
    return images


@router.get("/{img_id}", response_model=schemas.Image)
async def get_image_by_id(img_id: int, db: Session = Depends(get_db)):
    db_image = crud.get_image_by_id(db=db, image_id=img_id)
    if db_image is None:
        raise HTTPException(status_code=404, detail="Image not found")
    return db_image


@router.get("/title/{img_title}", response_model=list[schemas.Image])
async def get_images_by_title(img_title: str, db: Session = Depends(get_db)):
    db_image = crud.get_images_by_title(db=db, image_title=img_title)
    if db_image is None:
        raise HTTPException(status_code=404, detail="Image not found")
    return db_image


@router.get("/user/{user_id}", response_model=list[schemas.Image])
async def get_images_by_user_id(user_id: int, db: Session = Depends(get_db)):
    db_image = crud.get_images_by_user_id(db=db, user_id=user_id)
    if db_image is None:
        raise HTTPException(status_code=404, detail="Image not found")
    return db_image


# Post Routes
@router.post("/new", response_model=schemas.Image)
async def create_image(image: schemas.ImageCreate, db: Session = Depends(get_db)):
    return crud.create_image(db=db, image=image, usr_id=image.user_id)