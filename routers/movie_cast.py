from typing import Optional
from fastapi import APIRouter,Path, Query, Depends
from pydantic import BaseModel, Field
from fastapi.responses import  JSONResponse
from fastapi.encoders import jsonable_encoder


from config.database import Session
from schemas.movie_cast import MovieCast as MovieCastSchemas
from service.movie_cast import MovieCastService


movie_cast_router = APIRouter()


@movie_cast_router.get('/movie_cast/{id_movie}', tags=['movie_cast'],response_model=list[MovieCastSchemas],status_code=200)
def get_movie_cast(id_movie:int = Path(ge=1,le=2000)):
    db = Session()
    result = MovieCastService(db).get_movie_cast(id_movie)
    if not result:
        return JSONResponse(content={"message":"No se ha encontrado el registro","status_code":"404"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)


@movie_cast_router.post('/movie_cast', tags=['movie_cast'],response_model=dict,status_code=201)
def create_cast(cast:MovieCastSchemas)->dict:
    db = Session()
    MovieCastService(db).create_movie_cast(cast)
    return JSONResponse(content={"message":"Se ha registrado el actor","status_code":201})


@movie_cast_router.delete('/movie_cast/{id}',tags=['movie_cast'])
def delete_movie_cast(id:int):
        db = Session()
        result = MovieCastService(db).delete_movie_cast(id)
        if not result:
            return JSONResponse(status_code=404,content={"message":"No found"})
        return JSONResponse(content="Delete movie succefull", status_code=200) 


@movie_cast_router.put('/movie_cast/{id}',tags=['movie_cast'])
def update_movie_cast(id:int, data:MovieCastSchemas):
    db =  Session()
    result = MovieCastSchemas(db).update_movie_cast(id, data)
    if not result:
        return JSONResponse(content={"message":"No se ha encontrado el registro","status_code":"404"})
    return JSONResponse(content={"message":"Se ha modificado la pelicula con id: "+ str(id)})            
