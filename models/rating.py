from sqlalchemy import Column, Integer, String,Foreignkey
from sqlalchemy.orm import relationship

from config.database import Base


class rating (Base):

    __tablename__ = "rating"
    mov_id = Column(Integer,Foreignkey("movies.id"))
    rev_id = Column(Integer,Foreignkey("reviewer.id"))