import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
from pymongo.errors import PyMongoError

MONGO_URL = os.getenv("MONGO_URL", "mongodb://mongo:27017")
DB_NAME = os.getenv("MONGO_DB", "moviesdb")

app = FastAPI(title="Movies API")
client = MongoClient(MONGO_URL, serverSelectionTimeoutMS=2000)
movies = client[DB_NAME]["movies"]


class Movie(BaseModel):
    title: str
    year: int
    rating: float | None = None


@app.get("/health")
def health():
    try:
        client.admin.command("ping")
    except PyMongoError:
        raise HTTPException(status_code=503, detail="database unavailable")
    return {"status": "ok"}


@app.get("/api/movies")
def list_movies():
    return list(movies.find({}, {"_id": 0}))


@app.post("/api/movies", status_code=201)
def add_movie(movie: Movie):
    movies.insert_one(movie.model_dump())
    return movie


@app.get("/api/ping")
def ping():
    return {"pong": True}
