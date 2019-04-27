from db import db
from datetime import datetime
from sqlalchemy import and_
from sqlalchemy.sql.expression import any_


class MovieModel(db.Model):
    __tablename__ = 'movies'

    tconst = db.Column('tconst', db.String, primary_key=True)
    titleType = db.Column('titleType', db.String)
    primaryTitle = db.Column('primaryTitle', db.String)
    originalTitle = db.Column('originalTitle', db.String)
    isAdult = db.Column('isAdult', db.Boolean)
    startYear = db.Column('startYear', db.DateTime)
    endYear = db.Column('endYear', db.DateTime)
    runtimeMinutes = db.Column('runtimeMinutes', db.Integer)
    genres = db.Column('genres', db.ARRAY(db.String))

    @classmethod
    def find_by_tconst(cls, _tconst):
        return cls.query.filter_by(tconst=_tconst).first()

    @classmethod
    def find_by_name(cls, _username: str):
        return cls.query.filter_by(username=_username).first()

    @classmethod
    def find_by_year(cls, _year: str):
        return cls.query.filter_by(startYear=datetime.strptime(_year, '%Y')).order_by(MovieModel.primaryTitle)

    @classmethod
    def find_by_year_and_genere(cls, _year, _genre):
        return cls.query.filter(
                                    and_(
                                        _genre == any_(cls.genres),
                                        cls.startYear == datetime.strptime(_year, '%Y')
                                        )
                                   ).order_by(cls.primaryTitle)

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

