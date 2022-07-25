from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

from project.setup.db import models


class Genre(models.Base):
    __tablename__ = 'genres'

    name = Column(String(100), unique=True, nullable=False)


class Director(models.Base):
    __tablename__ = 'director'

    name = Column(String(100), unique=True, nullable=False)


class Movie(models.Base):
    __tablename__ = 'movie'

    title = Column(String(100), unique=True, nullable=False)
    description = Column(String(100), nullable=False)
    trailer = Column(String(100), nullable=False)
    year = Column(Integer, nullable=False)
    rating = Column(Float, nullable=False)
    genre_id = Column(Integer, ForeignKey(f'{Genre.__tablename__}.id'), nullable=False)
    director_id = Column(Integer, ForeignKey(f'{Director.__tablename__}.id'), nullable=False)
    genre = relationship('Genre')
    director = relationship('Director')


class User(models.Base):
    __tablename__ = 'user'

    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    name = Column(String(100))
    surname = Column(String(100))
    favourite_genre = Column(Integer, ForeignKey(f'{Genre.__tablename__}.id'))
    genre = relationship('Genre')
