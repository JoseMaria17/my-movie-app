
""" from typing import Optional """
from fastapi import APIRouter,Path, Query, Depends
from pydantic import BaseModel, Field
from fastapi.responses import  JSONResponse
from fastapi.encoders import jsonable_encoder

""" from models.genres import Genres as GenresModel """
from schemas.genres import Genres as GenresSchemas
from config.database import Session
from service.genres import GenresService


genres_router = APIRouter()

@genres_router.get('/genres', tags=['genres'], response_model=GenresSchemas, status_code=200)
def get_genres():
    db=Session()
    result=GenresService(db).get_genres()
    return JSONResponse(content=jsonable_encoder(result), status_code=200)


""" @genres_router.get('/genres', tags=['genres'], response_model=GenresSchemas, status_code=200)
def get_genres_for_title(genres:str):
    db=Session()
    result=GenresService(db).get_genres_for_title
    return JSONResponse(content=jsonable_encoder(result), status_code=200) """


@genres_router.post('/genres', tags=['genres'], status_code=201, response_model=dict)
def create_genres(genres:GenresSchemas) -> dict: 
    db=Session()
    GenresService(db).create_genres(genres)
    return  JSONResponse(content={"message":"Registro de genero exitoso","status_code":"404"})