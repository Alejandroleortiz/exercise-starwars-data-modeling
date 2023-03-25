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
    email = Column(String(120), nullable=False)
    suscription_date = Column(String, nullable=False)

class Character(Base):
    __tablename__ = 'character'

    uid = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    description = Column(String(200), nullable=False)

class Planet(Base):
    __tablename__ = 'planet'

    uid = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    description = Column(String(200), nullable=False)

class Favorite_character(Base):
    __tablename__ = 'favorite_character'

    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.uid'), primary_key=True)
    user = relationship(User)
    character = relationship(Character)

class Favorite_planet(Base):
    __tablename__ = 'favorite_planet'

    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.uid'), primary_key=True)
    user = relationship(User)
    planet = relationship(Planet)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
