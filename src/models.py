import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(120), unique=True, nullable=False)
    password = Column(String(120), nullable=False)
    name = Column(String(120), nullable=False)
    last_name = Column(String(120), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    suscription_date = Column(String, nullable=False)

class Favorite(Base):
    __tablename__ = 'favorite'

    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('character.uid'))
    planet_id = Column(Integer, ForeignKey('planet.uid'))

class Character(Base):
    __tablename__ = 'character'

    uid = Column(Integer, unique=True)
    name = Column(String(150), nullable=False)
    description = Column(String(200), nullable=False)

class Planet(Base):
    __tablename__ = 'planet'

    uid = Column(Integer, unique=True)
    name = Column(String(150), nullable=False)
    description = Column(String(200), nullable=False)



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
