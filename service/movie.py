from models.movie import Movie as MovieModel



class MovieService():

    def __init__(self,db) -> None:
        self.db = db

    def get_movies(self):
        result = self.db.query(MovieModel).all()
        return result

    def create_movies(self, movies:MovieModel):
        new_movie= MovieModel( 
        id=movies.id ,
        title= movies.title,
        overview=movies.overview,
        year=movies.year,
        time=movies.time,
        date_release=movies.date_release,
        release_contry=movies.release_contry
        )
        self.db.add(new_movie)
        self.db.commit()
        return  
         

    def get_movie_by_id(self, id:int):
        return self.db.query(MovieModel).filter(MovieModel.id == id).first()


    def get_movies_by_title(self,title:str):
        result = self.db.query(MovieModel).filter(MovieModel.title == title).all()
        return result     
       

    def delete_movies(self,id:int):
        movie=self.get_movie_by_id(id)
        if not movie:
            return None
        self.db.delete(movie)
        self.db.commit()
        return movie


    def update_movie(self,id:int, data:MovieModel):
        movie = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        movie.title = data.title
        movie.overview = data.overview
        movie.year = data.year
        movie.time = data.time
        movie.date_release = data.date_release
        movie.release_contry = data.release_contry
        self.db.commit()
        return data

    """ 

          

    def create_movie_title(self, movie:Movie):
        new_movie = MovieModel(
        title=movie.title,
        overview = movie.overview,
        year = movie.year,
        time = movie.time,
        date_release = movie.date_release,
        release_contry = movie.release_contry
        )
        self.db.add(new_movie)
        self.db.commit()
        return 

    def update_movie(self,id:int, data:Movie):
        movie = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        movie.title = data.title
        movie.overview = data.overview
        movie.year = data.year
        movie.time = data.time
        movie.date_release = data.date_release
        movie.release_contry = data.release_contry
        self.db.commit()
        return

    def delete_movie(self,id:int,data:Movie):
        self.db.delete(data)
        self.db.commit


 """
