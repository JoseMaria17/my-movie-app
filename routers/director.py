from fastapi import APIRouter
from config.database import Session
from service.director import DirectorService
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

director_router=APIRouter()

@director_router.get('/directors', tags=['directors','movies'], status_code=200)
def get_directors():
    db=Session()
    result= DirectorService(db).get_directors()
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

    



