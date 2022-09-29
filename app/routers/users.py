from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db.main import SessionLocal
from ..db import crud, schemas
from ..auth.auth import AuthHandler
from ..auth.schemas import AuthDetails

# Database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Auth Handler
auth_handler = AuthHandler()

router = APIRouter(
    prefix="/user"
)


# Get Routes
@router.get("/all", response_model=list[schemas.User])
async def get_all_users(skip: int = 0, limit: int = 0, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/{user_id}", response_model=schemas.User)
async def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id)
    # print(username)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/username/{username}", response_model=schemas.User)
async def get_user_by_username(username: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/email/{email}", response_model=schemas.User)
async def get_user_by_email(email: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


# Post Routes
@router.post("/new", response_model=schemas.User, status_code=201)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@router.post("/login")
async def login(auth_details: AuthDetails, db: Session = Depends(get_db)):
    user = crud.get_user_by_username(db, username=auth_details.username)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username")
    if not auth_handler.verify_password(auth_details.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid password")
    token = auth_handler.encode_token(user.username)
    return { "token": token }

# Delete Route
@router.delete("/delete/{username}")
async def delete_user_by_username(username: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db=db, username=username)
    if db_user:
        return crud.delete_user_by_username(db=db, username=username)
    else:
        raise HTTPException(status_code=404, detail="User not found")