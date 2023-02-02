from sqlalchemy import Column, Integer, String, Foreignkey
from sqlalchemy.orm import relationship

from config.database import Base


class reviewer(Base):

    __tablename__ = "reviewer"
    id= Column(Integer,primary_key = True)
    rev_name = Column(String)
   