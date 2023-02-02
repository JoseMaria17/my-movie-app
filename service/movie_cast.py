from models.movie_cast import MovieCast as MovieCastModel



class MovieCastService():

    def __init__(self,db) -> None:
        self.db = db


    def get_movie_cast(self,id_movie:int):
        result = self.db.query(MovieCastModel).filter(MovieCastModel.movie_id == id_movie).all()
        return result


    def create_movie_cast(self, movie_cast: MovieCastModel):
        new_cast = MovieCastModel(
            actor_id = movie_cast.actor_id,
            movie_id = movie_cast.movie_id,
            role = movie_cast.role
        )
        self.db.add(new_cast)
        self.db.commit()
        return


    def delete_movie_cast(self, id:int):
        result=self.db.query(MovieCastModel).filter(MovieCastModel.id == id).delete()
        self.db.commit()
        return result  


    def update_movie_cast(self,id:int, data:MovieCastModel):
        movie_cast = self.db.query(MovieCastModel).filter(MovieCastModel.id == id).first()
        movie_cast.actor_id = data.actor_id
        movie_cast.movie_id = data.movie_id
        movie_cast.role = data.role
        self.db.commit()
        return data       