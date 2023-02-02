from models.genres import Genres as GenresModel


class GenresService():
    def __init__(self,db) -> None:
        self.db = db

    def get_genres(self):
        result = self.db.query(GenresModel).all()
        return result

    #def get_genres_for_id(self, id):
        #result=self.db.query(GenresModel).filter(GenresModel.id==id).first()     
        #return result 


    #def get_genres_for_title(self, title):
        #result=self.db.query(GenresModel).filter(GenresModel.title == title).first()    
        #return result


    def create_genres(self, genres:GenresModel):
        new_gender= GenresModel( 
        gen_id=genres.gen_id,        
        gen_title=genres.gen_title
        )
        self.db.add(new_gender)
        self.db.commit()
        return




""" 
    def create_actor(self,actor:ActorMoldel):
        new_actor = ActorMoldel(
        actor_first_name = actor.actor_first_name ,
        actor_last_name = actor.actor_last_name,
        actor_gender = actor.actor_gender,    
        )
        self.db.add(new_actor)
        self.db.commit()
        return """