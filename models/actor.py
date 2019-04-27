from numpy.testing._private.decorators import knownfailureif
from sqlalchemy.dialects import postgresql as pg
from sqlalchemy.sql.expression import any_

from db import db

class ActorModel(db.Model):
    __tablename__ = 'actors'

    nconst = db.Column('nconst', db.String(10), primary_key=True)
    primaryName = db.Column('primaryName', db.String)
    birthYear = db.Column('birthYear', db.DateTime)
    deathYear = db.Column('deathYear', db.DateTime)
    primaryProfession = db.Column('primaryProfession', db.ARRAY(db.String))
    knownForTitles = db.Column('knownForTitles', pg.ARRAY(db.String))

    @classmethod
    def find_by_nconst(cls, nconst: int):
        return cls.query.filter_by(nconst=nconst).first()

    @classmethod
    def find_by_primaryName(cls, _primaryName: str):
        return cls.query.filter_by(primaryName=_primaryName).first()

    @classmethod
    def find_by_movie(cls, _knownForTitles: str):
        return cls.query.filter(_knownForTitles == any_(cls.knownForTitles)).all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

        