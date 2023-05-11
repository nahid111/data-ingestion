from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import expose, BaseView, ModelView, has_access
from flask_appbuilder.api import BaseApi
from . import appbuilder, db
from .models import Movie, Director, Genre
from .services import save_to_file
from .helpers import ingest_data


# Application wide 404 error handler
@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", base_template=appbuilder.base_template, appbuilder=appbuilder), 404


class GenreView(ModelView):
    datamodel = SQLAInterface(Genre)


class DirectorView(ModelView):
    datamodel = SQLAInterface(Director)


class MoviesView(ModelView):
    datamodel = SQLAInterface(Movie)
    related_views = [GenreView, DirectorView]
    list_columns = ['name', 'imdb_id', 'directors', 'genres', 'publish_date']


class IngestView(BaseView):
    default_view = 'ingest'

    @expose('/ingest/')
    @has_access
    def ingest(self):
        return self.render_template('ingest.html')


class FetchApi(BaseApi):
    @expose('/fetch')
    def greeting(self):
        save_to_file()
        return self.response(200, status="Done")


class IngestApi(BaseApi):
    @expose('/ingest')
    def greeting(self):
        ingest_data(from_file=True)
        return self.response(200, status="Done")


appbuilder.add_api(FetchApi)
appbuilder.add_api(IngestApi)
appbuilder.add_view(IngestView, "Ingest")
appbuilder.add_view(MoviesView, "Movies", icon="fa-film", category="Movie Data", category_icon='fa-database')
appbuilder.add_view(GenreView, "Genres", icon="fa-tags", category="Movie Data", category_icon='fa-database')
appbuilder.add_view(DirectorView, "Directors", icon="fa-user", category="Movie Data", category_icon='fa-database')

db.create_all()
