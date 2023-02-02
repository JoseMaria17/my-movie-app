from fastapi import APIRouter,Path, Query, Depends
from fastapi.responses import  JSONResponse
from typing import  List
from fastapi.encoders import jsonable_encoder

from schemas.actor import Actor as ActorSchemas
from config.database import Session
from service.actor import ActorService


actor_router = APIRouter()

@actor_router.get('/actors',tags=['actors'], response_model=ActorSchemas, status_code= 200)
def get_actor() ->ActorSchemas:   
    db = Session()
    result = ActorService(db).get_actors()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)


@actor_router.post('/actors', tags=['actors'], status_code=201 , response_model=dict)
def create_actor(actor:ActorSchemas) ->dict:
    db= Session()
    ActorService(db).create_actor(actor)
    return JSONResponse(content={'message':'actor save in data base'})


@actor_router.delete('/actors/{id}',tags=['actors'])
def delete_actors(id:int):
        db = Session()
        result = ActorService(db).delete_actors(id)
        if not result:
            return JSONResponse(status_code=404,content={"message":"No found"})
        return JSONResponse(content="Delete movie succefull", status_code=200)    


@actor_router.put('/actors{id}',tags=['actors'])
def update_actors(id:int, data:ActorSchemas):
    db =  Session()
    result = ActorService(db).update_actors(id, data)
    if not result:
        return JSONResponse(content={"message":"No se ha encontrado el registro","status_code":"404"})
    return JSONResponse(content={"message":"Se ha modificado la pelicula con id: "+ str(id)})  
