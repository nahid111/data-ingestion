from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship


class Genre(Model):
    __tablename__ = "genres"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(150), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Director(Model):
    __tablename__ = "directors"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(150), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Movie(Model):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    imdb_id = Column(String(150), unique=True, nullable=False)
    name = Column(String(150), unique=True, nullable=False)
    publish_date = Column(Date)
    genres = relationship('Genre', secondary="movies_genres", backref='movies')
    directors = relationship('Director', secondary="movies_directors", backref='movies')

    def __repr__(self):
        return self.name


class MovieDirector(Model):
    __tablename__ = "movies_directors"
    movie_id = Column(Integer, ForeignKey("movies.id"), primary_key=True)
    director_id = Column(Integer, ForeignKey("directors.id"), primary_key=True)


class MovieGenre(Model):
    __tablename__ = "movies_genres"
    movie_id = Column(Integer, ForeignKey("movies.id"), primary_key=True)
    genre_id = Column(Integer, ForeignKey("genres.id"), primary_key=True)
