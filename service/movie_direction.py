from models.movie_direction import movieDirection

class MovieDirectionService():

    def __init__(self,db) -> None:
        self.db = db


    def get_movie_direction(self,id_movie:int):
        result = self.db.query(movieDirection ).filter(movieDirection.movie_id == id_movie).all()
        return result


    def create_movie_direction(self, movie_direction: movieDirection):
        new_cast = movieDirection(
        dir_id= movie_direction.dir_id,
        movie_id = movie_direction.movie_id
            
        )
        self.db.add(new_cast)
        self.db.commit()
        return