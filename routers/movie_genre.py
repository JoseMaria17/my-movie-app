from typing import Optional
from fastapi import APIRouter,Path, Query, Depends
from pydantic import BaseModel, Field
from fastapi.responses import  JSONResponse
from fastapi.encoders import jsonable_encoder


from config.database import Session
from schemas.movie_genre import MovieGenre as MovieGenreSchemas
from service.movie_genre import MovieGenreService


movie_genre_router = APIRouter()


@movie_genre_router.get('/movie_genre/{id_movie}', tags=['movie_genre'],response_model=list[MovieGenreSchemas],status_code=200)
def get_movie_genre(id_movie:int = Path(ge=1,le=2000)):
    db = Session()
    result = MovieGenreService(db).get_movie_genre(id_movie)
    if not result:
        return JSONResponse(content={"message":"No se ha encontrado el registro","status_code":"404"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)


@movie_genre_router.post('/movie_genre', tags=['movie_genre'],response_model=dict,status_code=201)
def create_movie_genre(genre:MovieGenreSchemas)->dict:
    db = Session()
    MovieGenreService(db).create_movie_genre(genre)
    return JSONResponse(content={"message":"Se ha registrado el genero","status_code":201})