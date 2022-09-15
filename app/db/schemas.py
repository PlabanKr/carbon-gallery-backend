from datetime import date
from pydantic import BaseModel
from typing import Union


class ImageBase(BaseModel):
    title: str
    caption: str
    tag: list[str] = []
    upload_date: date
    likes: int
    user_id: int


class ImageCreate(ImageBase):
    link: str


class Image(ImageBase):
    id: int

    class Config:
        orm_mode = True
    

class UserBase(BaseModel):
    name: str
    email: str
    bio: str
    social_media: str
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    images: list[Image] = []

    class Config:
        orm_mode = True