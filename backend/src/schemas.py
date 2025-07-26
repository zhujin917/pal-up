from pydantic import BaseModel
from datetime import date

class UserBase(BaseModel):
    email: str
class UserCreate(UserBase):
    email: str
    password: str
    avatar_id: str
    nickname: str
    sex: str
    mbti: str
    birthyear: int
class UserLogin(UserBase):
    password: str


class UserProfileCreate(BaseModel):

    class Config:
        from_attributes = True

class TripCreate(BaseModel):
    activity_id: int
    date: str
    text: str
    is_public: bool

class ActivityCreate(BaseModel):
    title: str
    introduction: str
    city: str
    begin_time: str
    end_time: str

class UpdateTripPublic(BaseModel):
    trip_id: int
    is_public: bool