from flask_restful import Resource
from datetime import datetime
from flask import request
import csv

from models.movie import MovieModel
from models.actor import ActorModel


class LoadMovie(Resource):
    @classmethod
    def get(cls):

        with open('title_data.tsv') as file:
            dict_records = csv.DictReader(file, delimiter='\t')
            for record in dict_records:
                movie = MovieModel(
                            tconst= record['tconst'],
                            titleType = record['titleType'],
                            primaryTitle = record['primaryTitle'],
                            originalTitle = record['originalTitle'],
                            isAdult = False if record['isAdult'] =='0' else True,
                            startYear = datetime.strptime(record['startYear'], '%Y') if not record['startYear'] == '\\N' else None,
                            endYear =datetime.strptime(record['endYear'], '%Y') if not record['endYear'] == '\\N' else None,
                            runtimeMinutes = 0 if record['runtimeMinutes'] =='\\N' else record['runtimeMinutes'],
                            genres = record['genres'].split(',')
                            )
                movie.save_to_db()


class MoviesFromYear(Resource):
    @classmethod
    def get(cls,year: int):
        movies_list = MovieModel.find_by_year(str(year))
        for movie in movies_list:
            print(f'{movie.primaryTitle} - {movie.genres}  ')
            actors = ActorModel.find_by_movie(movie.tconst)
            counter = 0
            for actor in actors:
                counter += 1
                print(f' \t {counter} - {actor.primaryName}')


class MoviesFromYearAndGenre(Resource):
    @classmethod
    def post(cls):
        data =request.get_json()
        year = data.get('year')
        genre = data.get('genre')
        movies_list = MovieModel.find_by_year_and_genere(year, genre)
        for movie in movies_list:
            print(f'{movie.primaryTitle} - {movie.genres}  ')
            actors = ActorModel.find_by_movie(movie.tconst)
            counter = 0
            for actor in actors:
                counter += 1
                print(f' \t {counter} - {actor.primaryName}')









