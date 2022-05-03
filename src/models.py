import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class User(Base):
    __tablename__= 'usuario'
    id= Column(Integer, primary_key=True)
    password = Column(String(250))
    email = Column(String(250))

class Favoritos_personaje(Base):
    __tablename__= 'favoritos_personaje'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('usuario.id'))
    personaje_id= Column(Integer, ForeignKey('personaje.id'))

class Favoritos_planetas(Base):
    __tablename__= 'favoritos_planetas'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('usuario.id'))
    planeta_id= Column(Integer, ForeignKey('planetas.id'))

class Favoritos_starships(Base):
    __tablename__= 'favoritos_starships'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('usuario.id'))
    starships_id= Column(Integer, ForeignKey('starships.id'))

class Personaje(Base):
    __tablename__= 'personaje'
    id = Column(Integer, primary_key=True)
    height = Column(String(250))
    mass = Column(String(250))
    hair_color = Column(String(250))
    eye = Column(String(250))
    birth_year = Column(String(250))
    gender = Column(String(250))

class Planetas(Base):
    __tablename__= 'planetas'
    id = Column(Integer, primary_key=True)
    model = Column(String(250))
    starship = Column(String(250))
    cost_in_credits = Column(String(250))
    length = Column(String(250))
    crew = Column(String(250))
    passengers = Column(String(250)) 
    max_atmosphering_speed = Column(String(250))
    hyperdrive_rating = Column(String(250))
    mGLT = Column(String(250))
    cargo_capacity = Column(String(250))
    consumables = Column(String(250))

class Starship(Base):
    __tablename__= 'starships'
    id = Column(Integer, primary_key=True)
    model = Column(String(250))
    starship_class = Column(String(250))
    cost_in_credits = Column(String(250))
    length = Column(String(250))
    crew = Column(String(250))
    passengers = Column(String(250))
    max_atmosphering_speed = Column(String(250))
    hyperdrive_rating = Column(String(250))
    mGLT = Column(String(250))
    cargo_capacity = Column(String(250))
    consumables = Column(String(250))

 


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')