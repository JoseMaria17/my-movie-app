from fastapi import APIRouter,Path, Query, Depends
from fastapi.responses import  JSONResponse
from typing import  List
from fastapi.encoders import jsonable_encoder

from fastapi.security import HTTPBearer
from config.database import Session
from service.movie import MovieService
from schemas.movie import Movie as MovieSchemas

movie_router = APIRouter()




#@app.get('/movies',tags=['movies'],response_model=List[Movie],status_code=200, dependencies=[Depends(JWYBearer())])
@movie_router.get('/movies',tags=['movies'],response_model=MovieSchemas,status_code=200)
def get_movies():
    db = Session()
    result = MovieService(db).get_movies()
    return JSONResponse(content=jsonable_encoder(result), status_code=200)


@movie_router.get('/movies/{id}',tags=['movies'])
def get_movie_by_id(id:int = Path(ge=1,le=2000)):
    db = Session()
    result = MovieService(db).get_movie_by_id(id)
    if not result:
        return JSONResponse(status_code=404,content={"message":"No found"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200) 



@movie_router.get('/movies/title',tags=['movies'],response_model=List[MovieSchemas],status_code=200)
def get_movies_by_title(title:str = Query(min_length=3,max_length=15)):
    db = Session()
    result = MovieService(db).get_movies_by_title(title)
    if not result:
        return JSONResponse(status_code=404,content={"message":"No found"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)



@movie_router.post('/movies',tags=['movies'],status_code=201,response_model=dict)
def create_movies(movies:MovieSchemas)->dict:
    db = Session()
    MovieService(db).create_movies(movies)
    return JSONResponse(content={"message":"Se ha registrado la pelicula","status_code":201})



@movie_router.delete('/movies/{id}',tags=['movies'])
def delete_movies(id:int):
        db = Session()
        result = MovieService(db).delete_movies(id)
        if not result:
            return JSONResponse(status_code=404,content={"message":"No found"})
        return JSONResponse(content="Delete movie succefull", status_code=200)



@movie_router.put('/movies{id}',tags=['movies'])
def update_movie(id:int, data:MovieSchemas):
    db =  Session()
    result = MovieService(db).update_movie(id, data)
    if not result:
        return JSONResponse(content={"message":"No se ha encontrado el registro","status_code":"404"})
    return JSONResponse(content={"message":"Se ha modificado la pelicula con id: "+ str(id)})        


""" @movie_router.get('/movies/{id}',tags=['movies'])
def get_movie_by_id(id:int = Path(ge=1,le=2000)):
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404,content={"message":"No found"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)


    
@movie_router.get('/movies/',tags=['movies'],response_model=List[Movie],status_code=200)
def get_movies_by_release_contry(release_contry:str = Query(min_length=3,max_length=15)):
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.release_contry == release_contry).all()
    if not result:
        return JSONResponse(status_code=404,content={"message":"No found"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)



@movie_router.post('/movies',tags=['movies'],status_code=201,response_model=dict)
def create_movie(movie:Movie)->dict:
    db = Session()
    MovieService.create_movie(db,movie)
    return JSONResponse(content={"message":"Se ha registrado la pelicula","status_code":201})



@movie_router.put('/movies{id}',tags=['movies'])
def update_movie(id:int,movie:Movie):
    db =  Session
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(content={"message":"No se ha encontrado el registro","status_code":"404"})
    MovieService(db).update_movie(id,movie)
    return JSONResponse(content={"message":"Se ha modificado la pelicula con id: {id}"})

   

@movie_router.delete('/movies/{id}',tags=['movies'])
def delete_movie(id:int):
        db = Session()
        result = MovieService(db).get_movie(id)
        if not result:
            return JSONResponse(status_code=404,content={"message":"No found"})
        return JSONResponse(content="Delete movie", status_code=200)
     """