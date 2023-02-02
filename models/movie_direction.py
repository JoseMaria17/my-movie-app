from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from config.database import Base


class movieDirection(Base):

    __tablename__ = "movie_direction"
    id = Column(Integer, primary_key=True, index=True)
    dir_id = Column(Integer,ForeignKey("director.id"))
    movie_id = Column(Integer,ForeignKey("movie.id"))