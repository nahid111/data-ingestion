from datetime import datetime
from . import db
from .models import Movie, Director, Genre
from .services import get_data, read_data_from_file


def ingest_data(from_file=False):
    print("Ingestion Started")
    if from_file:
        data = read_data_from_file()
    else:
        data = get_data()

    for record in data:
        p_date = datetime.fromisoformat(record['pubdate']['value'][:-1] + '+00:00')

        # create genre
        genre = db.session.query(Genre).filter(Genre.name == record['genreLabel']['value']).first()
        if not genre:
            genre = Genre(name=record['genreLabel']['value'])
            db.session.add(genre)

        # create director
        director = db.session.query(Director).filter(Director.name == record['directorLabel']['value']).first()
        if not director:
            director = Director(name=record['directorLabel']['value'])
            db.session.add(director)

        # create movie
        movie_by_name = db.session.query(Movie).filter(Movie.name == record['itemLabel']['value']).first()
        movie_by_imdb_id = db.session.query(Movie).filter(Movie.imdb_id == record['imdbId']['value']).first()
        if movie_by_name:
            movie = movie_by_name
        elif movie_by_imdb_id:
            movie = movie_by_imdb_id
        else:
            movie = Movie(imdb_id=record['imdbId']['value'], name=record['itemLabel']['value'], publish_date=p_date)
            db.session.add(movie)

        # Assign Director
        if director.name not in movie.directors:
            movie.directors.append(director)

        # Assign genre
        if genre.name not in movie.genres:
            movie.genres.append(genre)

        db.session.commit()

    print("Ingestion Complete")
