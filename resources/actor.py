from flask_restful import Resource
from flask import request
from datetime import datetime
import csv

from models.actor import ActorModel
from models.movie import MovieModel


class LoadActors(Resource):
    @classmethod
    def get(cls):

        with open('name_data.tsv') as file:
            dict_records = csv.DictReader(file, delimiter='\t')
            for record in dict_records:
                record_exist = ActorModel.find_by_nconst(record['nconst'])
                if not record_exist:
                    actor = ActorModel(
                                nconst=record['nconst'],
                                primaryName=record['primaryName'],
                                birthYear= datetime.strptime(record['birthYear'], '%Y') if not record['birthYear'] == '\\N' else None,
                                deathYear= datetime.strptime(record['deathYear'], '%Y') if not record['deathYear'] == '\\N' else None,
                                primaryProfession=record['primaryProfession'].split(','),
                                knownForTitles= record['knownForTitles'].split(',')
                    )
                    actor.save_to_db()


class KnownActor(Resource):
    @classmethod
    def post(cls):
        data = request.get_json()
        actor = ActorModel.find_by_nconst(data.get('name'))
        print(actor.knownForTitles)


class PlayInMovies(Resource):
    @classmethod
    def post(cls):
        data = request.get_json()
        actor = ActorModel.find_by_primaryName(data.get('name'))
        print(f' {actor.primaryName} play in:')
        counter = 1
        for movie_id in actor.knownForTitles:
            movie = MovieModel.find_by_tconst(movie_id)
            print(f'\t{counter} - {movie.originalTitle}')
            counter +=1

