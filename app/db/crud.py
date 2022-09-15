from sqlalchemy.orm import Session

from . import models, schemas


# user crud functions
def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + 'notreallyhashed'
    # shortcut code -> **user.dict()
    db_user = models.User(
        name = user.name,
        email = user.email,
        bio = user.bio,
        username = user.username,
        social_media = user.social_media,
        hashed_password = fake_hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# image crud functions
def get_image_by_id(db: Session, image_id: int):
    return db.query(models.Image).filter(models.Image.id == image_id).first()


def get_images_by_user_id(db: Session, user_id: int, limit: int = 100):
    return db.query(models.Image).filter(models.Image.user_id == user_id).limit(limit).all()


def get_images_by_title(db: Session, image_title: str, limit: int = 100):
    return db.query(models.Image).filter(models.Image.title == image_title).limit(limit).all()


def get_images(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Image).offset(skip).limit(limit).all()


def create_image(db: Session, image: schemas.ImageCreate, user_id: int):
    db_image = models.Image(**image.dict(), user_id = user_id)
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image
    