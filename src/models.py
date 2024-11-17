import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    email = Column(String, unique=True)
    password = Column(String)  
    fecha_registro = Column(String)

class Planeta(Base):
    __tablename__ = 'planetas'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)  
    diametro = Column(Integer)
    periodo_rotacion = Column(Integer)
    residentes = Column(Integer, ForeignKey('personajes.id'))
    peliculas = Column(Integer, ForeignKey('peliculas.id'))

class Personaje(Base):
    __tablename__ = 'personajes'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    altura = Column(Integer)
    planetas = Column(Integer, ForeignKey('planetas.id'))
    peliculas = Column(Integer, ForeignKey('peliculas.id'))

class Pelicula(Base):
    __tablename__ = 'peliculas'
    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    episodio_id = Column(Integer)
    planeta = Column(Integer, ForeignKey('planetas.id'))  
    personajes = Column(Integer, ForeignKey('personajes.id')) 

class Favorito(Base):
    __tablename__ = 'favoritos'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))  
    planeta_id = Column(Integer, ForeignKey('planetas.id'))  
    personajes_id = Column(Integer, ForeignKey('personajes.id')) 
    tipo = Column(String)
    usuario = relationship("Usuario", back_populates="favoritos")


try:
    result = render_er(Base, 'diagrama_star_wars.png')
    print("¡Diagrama generado exitosamente! Busca el archivo diagrama_star_wars.png")
except Exception as e:
    print("Hubo un problema al generar el diagrama:", e)