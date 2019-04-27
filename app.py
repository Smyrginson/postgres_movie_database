from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api


from resources.actor import LoadActors, KnownActor, PlayInMovies
from resources.movie import LoadMovie, MoviesFromYear, MoviesFromYearAndGenre
from db import db

app = Flask(__name__)


app.config['SECRET_KEY'] = 'secret!'
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://kinomaniak:filmy@localhost/movies'
# app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://kinomaniak:filmy@oniongeek.com/movies'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

api = Api(app)
migrate = Migrate(app, db)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(LoadActors, '/loadactors')
api.add_resource(LoadMovie, '/loadmovies')
api.add_resource(KnownActor, '/known')
api.add_resource(MoviesFromYear, '/year/<int:year>')
api.add_resource(MoviesFromYearAndGenre, '/yearandgenre')
api.add_resource(PlayInMovies, '/playinmovie')


if __name__ == '__main__':
    db.init_app(app)
    app.run(host='localhost', port=5000)

