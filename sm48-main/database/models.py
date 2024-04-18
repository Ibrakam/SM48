from sqlalchemy import (Column, Integer, String, BigInteger,
                        ForeignKey, Float, Date, DateTime, Boolean)
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    phone_number = Column(String, nullable=False, unique=True)
    user_city = Column(String, nullable=True)
    password = Column(String)
    reg_date = Column(DateTime)


class UserPost(Base):
    __tablename__ = "user_posts"
    id = Column(Integer, autoincrement=True, primary_key=True)
    main_text = Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    reg_date = Column(DateTime)
    user_fk = relationship(User, lazy="subquery")


class PostPhoto(Base):
    __tablename__ = "post_photos"
    id = Column(Integer, autoincrement=True, primary_key=True)
    post_id = Column(Integer, ForeignKey("user_posts.id"))
    photo_path = Column(String, nullable=False)
    reg_date = Column(DateTime)
    post_fk = relationship(UserPost, lazy="subquery")


class Hashtag(Base):
    __tablename__ = "hashtags"
    id = Column(Integer, autoincrement=True, primary_key=True)
    hashtag_name = Column(String, nullable=False, unique=True)
    post_id = Column(Integer, ForeignKey("user_posts.id"))
    reg_date = Column(DateTime)
    post_fk = relationship(UserPost, lazy="subquery")


class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, autoincrement=True, primary_key=True)
    post_id = Column(Integer, ForeignKey("user_posts.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    text = Column(String, nullable=False)
    reg_date = Column(DateTime)
    user_fk = relationship(User, lazy="subquery")
    post_fk = relationship(UserPost, lazy="subquery")
