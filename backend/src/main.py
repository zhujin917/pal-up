import datetime
import hashlib
import json
import os
from concurrent.futures import ThreadPoolExecutor, Future
from datetime import date, time
from http.client import responses
import re
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import time
from PIL import Image
from anyio import Path
from databases import Database
from fastapi import FastAPI, Depends, File, UploadFile, Response, HTTPException, Cookie, Request, middleware
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel
from typing import List, Any, Generator, Coroutine
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker, Session

from src import ai
from src.ai import get_tags, get_partners
from src.models import UserProfile, Base, User, Activity, Trip
from src.schemas import UserProfileCreate, UserCreate, UserLogin, ActivityCreate, TripCreate, UpdateTripPublic

app = FastAPI()

database_url: str = os.environ.get("DATABASE_URL", "postgresql://adventurex:adventurex@localhost:5432/adventurex")

engine = create_engine(database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def get_db() -> Generator[Session, Any, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        


# @app.get("/")
# def read_index():
#     return FileResponse("./static/index.html")

# app.mount("/", StaticFiles(directory="static", html=True), name="static")

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    
    
    # 如果是静态文件，直接交给StaticFiles
    if request.url.path.startswith("/static"):
        return await call_next(request)
    if os.path.exists('./static'+request.url.path+'/'+"index.html"):
        return FileResponse('./static'+request.url.path+'/'+"index.html")
    if os.path.exists('./static'+request.url.path):
        return FileResponse('./static'+request.url.path)
    
    
    if request.url.path != "/api/login" and request.url.path != "/api/register" and request.url.path != "/api/avatar" and request.url.path != "/api/activity" and request.url.path != "/api/account":
        if request.cookies.get("user_id") is None:
            return Response(headers={"Location": "/login"}, status_code=403)
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.get("/api")
def read_root():
    return {"message": "Welcome to the AdventureX API"}

@app.post("/api/login")
async def login(response: Response, user: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter_by(email=user.email).first()
    response.set_cookie("user_id", str(user.id))


@app.post("/api/account")
def create_user(response: Response, user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(
        email=user.email,
        password=user.password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    user_id = db.query(User).filter_by(email=user.email).first().id

    db_profile = UserProfile(
        id=int(user_id),
        avatar_id=user.avatar_id,
        nickname=user.nickname,
        sex=user.sex,
        mbti=user.mbti,
        birthyear=user.birthyear,
    )

    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    db.refresh(db_user)
    response.set_cookie("user_id", str(db_user.id))
    return db_profile


@app.get("/api/account")
def get_user(response: Response,email: str, password: str,user_id: str | None = Cookie(default=None), db: Session = Depends(get_db)):
    user = db.query(User).filter_by(email=email).first()
    if user is None:
        raise HTTPException(status_code=403, detail="看看你的email")
    if user.password != password:
        raise HTTPException(status_code=403, detail="Invalid credentials")
    userProfile = db.query(UserProfile).filter_by(id=user.id).first()
    response.set_cookie("user_id", str(user.id))
    return userProfile

# 根据用户id获取用户信息
def get_userProfile_byid(user_id: int, db: Session = Depends(get_db)):
    # 从数据库中查询用户信息
    user = db.query(UserProfile).filter_by(id=user_id).first()
    # 返回查询到的用户信息
    return user


@app.post("/api/avatar")
async def upload_avatar(file: UploadFile, db: Session = Depends(get_db)):
    content = file.file.read()
    id = hashlib.md5(content).hexdigest()
    filename = id
    path = "./uploads/avatars/"
    filepath = path + filename + '.' + file.filename.split(".")[-1]
    if not os.path.exists(path):
        os.makedirs(path)
    if not os.path.isfile(filepath):
        with open(filepath, "wb") as f:
            f.write(content)
            image = Image.open(os.path.abspath(filepath))
            image.save(path + filename + ".webp", "WEBP")

    return {"avatar_id": id}


@app.get("/api/avatar")
def get_avatar(id: str, db: Session = Depends(get_db)):
    id = id
    filename = id

    with open(f"./uploads/avatars/{filename}.webp", "rb") as f:
        return Response(content=f.read(), media_type="image/webp")


@app.get("/api/activity")
def get_activity(city: str, title: str = None, db: Session = Depends(get_db)):
    activity = db.query(Activity).filter_by(city=city)
    if title:
        activity = activity.filter_by(title=title)
    return activity.all()


@app.post("/api/activity")
def create_activity(activity: ActivityCreate, user_id: int | None = Cookie(default=None), db: Session = Depends(get_db)):
    db_activity = Activity(
        owner=user_id,
        title=activity.title,
        city=activity.city,
        introduction=activity.introduction,
        begin_time=datetime.datetime.strptime(activity.begin_time, "%Y-%m-%d"),
        end_time=datetime.datetime.strptime(activity.end_time, "%Y-%m-%d"),
    )
    db.add(db_activity)
    db.commit()
    db.refresh(db_activity)
    return db_activity


@app.get("/api/activity/byid")
def get_activity_by_id(id: int, db: Session = Depends(get_db)):
    return db.query(Activity).filter_by(id=id).first()


@app.post("/api/trip")
def create_trip(trip: TripCreate, user_id: int | None = Cookie(default=None), db: Session = Depends(get_db)):
    db_trip = Trip(
        time=datetime.datetime.strptime(trip.date, "%Y-%m-%d"),
        owner=user_id,
        text=trip.text,
        activity_id=trip.activity_id,
        is_public=trip.is_public,
    )
    db.add(db_trip)
    db.commit()
    db.refresh(db_trip)
    return {"trip_id": db_trip.id}

@app.delete("/api/trip")
def delete_trip(trip_id: int, db: Session = Depends(get_db)):
    db.query(Trip).filter_by(id=trip_id).delete()
    db.commit()
    return {"msg": "success"}

@app.post("/api/trip/is_public")
def update_trip_is_public(public: UpdateTripPublic,db: Session = Depends(get_db)):
    db.query(Trip).filter_by(id=public.trip_id).update({"is_public": public.is_public})
    db.commit()
    return {"msg": "success"}

@app.get("/api/trip/is_public")
def get_trip_is_public(trip_id: int, db: Session = Depends(get_db)):
    return db.query(Trip).filter_by(id=trip_id).first().is_public



@app.get("/api/user/trips")
def get_trip(user_id: int | None = Cookie(default=None), db: Session = Depends(get_db)):
    trips = db.query(Trip).filter_by(owner=user_id).all()
    for trip in trips:
        trip.activity = db.query(Activity).filter_by(id=trip.activity_id).first()
    return trips


def to_list(text: str):
    return re.split(r'[;,]', text.strip("```json").strip("```").strip("\n").strip("[").strip("]"))


@app.get("/api/trip/tags")
def get_trip_tags(trip_id: int, db: Session = Depends(get_db)):
    trip = db.query(Trip).filter_by(id=trip_id).with_for_update().first()
    try:
        if trip.tags is None:
            trip.tags = to_list(get_tags(trip.text))
            db.commit()
    except:
        pass
    db.refresh(trip)
    return trip.tags


@app.get("/api/trip/byid")
def get_trip_by_id(trip_id: int, db: Session = Depends(get_db)):
    trip = db.query(Trip).filter_by(id=trip_id).first()
    return trip


def get_partners(trip_id: int, db: Session = Depends(get_db)):
    trip = db.query(Trip).filter_by(id=trip_id).with_for_update().first()
    if trip.partners is not None:
        return to_list(trip.partners)

    trips = db.query(Trip).filter_by(activity_id=trip.activity_id).filter_by(is_public=True).filter(Trip.id != trip.id)
    trips = trips.filter_by(time=trip.time).all()

    partner = []
    for othersTrip in trips:
        partner.append({"id": othersTrip.id, "tags": get_trip_tags(othersTrip.id, db)})

    trip.partners = ai.get_partners(get_trip_tags(trip.id, db), partner)
    db.commit()
    return partner

pool = ThreadPoolExecutor(max_workers=50, thread_name_prefix='Thread')
def get_suggestion(trip_id: int, db: Session = Depends(get_db)):
    trip = db.query(Trip).filter_by(id=trip_id).with_for_update().first()
    if trip.suggestions is not None:
        return trip.suggestions
    suggestions = []
    tasks = []


    for i in get_partners(trip_id, db):
        def add(partnerId:int,tripText:str,partnerText:str):
            suggestionsText=ai.get_suggestion(tripText, partnerText)
            suggestions.append({
                "trip_id": partnerId,
                "suggestion": suggestionsText
            })
            return True
        if type(i) is not int:
            try:
                i = i["id"]
            except:
                continue
        # tasks.append(pool.submit(add(i,trip.text,get_trip_by_id(i, db).text)))
        add(i,trip.text,get_trip_by_id(i, db).text)
        

    # for task in tasks:
    #     task.result()

    trip.suggestions = suggestions
    db.commit()
    return suggestions


@app.get("/api/suggestions")
def get_suggestions(trip_id: int, db: Session = Depends(get_db)):
    trip = db.query(Trip).filter_by(id=trip_id).with_for_update().first()
    suggestions = get_suggestion(trip_id, db)
    for suggestion in suggestions:
        suggestion["trip"]=get_trip_by_id(suggestion["trip_id"], db)
        suggestion["activity"]=get_activity_by_id(suggestion["trip"].activity_id, db)
        suggestion["user"]=get_userProfile_byid(suggestion["trip"].owner, db)
    return suggestions
