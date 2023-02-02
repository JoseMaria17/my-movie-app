from models.movie_genre import MovieGenre 

class MovieGenreService():

    def __init__(self,db) -> None:
        self.db = db


    def get_movie_genre(self,id_movie:int):
        result = self.db.query(MovieGenre ).filter(MovieGenre.movie_id == id_movie).all()
        return result


    def create_movie_genre(self, movie_genre: MovieGenre):
        new_cast = MovieGenre(
            movie_id = movie_genre.movie_id,
            gen_id= movie_genre.gen_id
            
        )
        self.db.add(new_cast)
        self.db.commit()
        return