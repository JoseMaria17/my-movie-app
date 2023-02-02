from pydantic import BaseModel


class Rating(BaseModel):
    mov_id: int 
    rev_id:int
    rev_stars:float
    num_o_ratings:int

    class Config:
        schema_extra={
            "example":{
                
                "mov_id": 1,
                "rev_id": 1,
                "rev_stars":5.5,
                "num_o_ratings":int
            }
        }