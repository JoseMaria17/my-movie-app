from typing import Optional
from fastapi import APIRouter,Path, Query, Depends
from pydantic import BaseModel, Field
from fastapi.responses import  JSONResponse
from fastapi.encoders import jsonable_encoder


from config.database import Session
from schemas.movie_direction import MovieDirection as MovieDirectionSchemas
from service.movie_direction import MovieDirectionService


movie_direction_router = APIRouter()


@movie_direction_router.get('/movie_direction/{id_movie}', tags=['movie_direction'],response_model=list[MovieDirectionSchemas],status_code=200)
def get_movie_direction(id_movie:int = Path(ge=1,le=2000)):
    db = Session()
    result = MovieDirectionService(db).get_movie_direction(id_movie)
    if not result:
        return JSONResponse(content={"message":"No se ha encontrado el registro","status_code":"404"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)


@movie_direction_router.post('/movie_direction', tags=['movie_direction'],response_model=dict,status_code=201)
def create_movie_direction(director:MovieDirectionSchemas)->dict:
    db = Session()
    MovieDirectionService(db).create_movie_direction(director)
    return JSONResponse(content={"message":"Se ha registrado el director","status_code":201})