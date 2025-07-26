from datetime import date
from typing import List
from sqlalchemy import ARRAY
from sqlalchemy import JSON

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user"


    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column() # MD5

    # activities: Mapped[List[int]] = mapped_column()


class Activity(Base):
    __tablename__ = "activity"

    id: Mapped[int] = mapped_column(primary_key=True,unique=True)
    title: Mapped[str] = mapped_column()
    introduction: Mapped[str] = mapped_column()
    city: Mapped[str] = mapped_column()
    begin_time: Mapped[date] = mapped_column()
    end_time: Mapped[date] = mapped_column()
    owner: Mapped[int] = mapped_column()



class UserProfile(Base):
    __tablename__ = "user_profile"

    id: Mapped[int] = mapped_column(primary_key=True,unique=True)
    avatar_id: Mapped[str] = mapped_column()
    nickname: Mapped[str] = mapped_column()
    sex: Mapped[str] = mapped_column()
    mbti: Mapped[str] = mapped_column()
    birthyear: Mapped[int] = mapped_column()


class Trip(Base):
    __tablename__ = "trip"

    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    activity_id: Mapped[int] = mapped_column()
    text: Mapped[str] = mapped_column()
    owner: Mapped[int] = mapped_column()
    time: Mapped[date] = mapped_column()

    tags: Mapped[list[str]] = mapped_column(JSON,nullable=True)
    partners: Mapped[list[int]] = mapped_column(JSON,nullable=True)
    suggestions: Mapped[list[str]] = mapped_column(JSON,nullable=True)

    is_public: Mapped[bool] = mapped_column()


