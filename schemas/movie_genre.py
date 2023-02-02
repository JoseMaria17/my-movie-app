from typing import Optional
from pydantic import BaseModel, Field



class MovieGenre(BaseModel):
        movie_id: int
        gen_id: int

        class Config:
            schema_extra = {
                "example":{
                    "movie_id":1,
                    "gen_id":1
                }
            }