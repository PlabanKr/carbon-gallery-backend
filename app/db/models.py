from sqlalchemy import ARRAY, Column, Integer, String
from sqlalchemy.types import Date
from sqlalchemy.orm import relationship
from .main import Base


# Data Models

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True, nullable=False)
    bio = Column(String)
    username = Column(String, unique=True, nullable=False)
    social_media = Column(String)
    hashed_password = Column(String)

    images = relationship("Image", back_populates="user")

    def __repr__(self):
        return f"User<id={self.id}, username={self.username}, email={self.email}>"


class Image(Base):
    __tablename__ = "image"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    link = Column(String, nullable=False)
    caption = Column(String)
    tag = Column(ARRAY(String))
    upload_date = Column(Date)
    likes = Column(Integer)

    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="images")
    
    def __repr__(self):
        return f"Image<id={self.id}, title={self.title}>"

