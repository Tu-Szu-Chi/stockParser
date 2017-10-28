from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

import twse.settings as settings


DeclarativeBase = declarative_base()


class Trades(DeclarativeBase):
    __tablename__ = "Trades"

    id = Column(Integer, primary_key=True)
    name = Column('name', String)
    tradeTotalShare = Column('tradeTotalShare', String)
    tradeTotalCount = Column('tradeTotalCount', String)
    tradeTotalPrice = Column('tradeTotalPrice', String)
    openPrice = Column('openPrice', Float)
    heightPrice = Column('heightPrice', Float)
    lowPrice = Column('lowPrice', Float)
    closePrice = Column('closePrice', Float)
    benefitRatio = Column('benefitRatio', Float)


def db_connect():

    return create_engine(URL(**settings.DATABASE))


def create_trades_table(engine):
    DeclarativeBase.metadata.create_all(engine)
