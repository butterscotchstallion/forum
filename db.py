from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()
engine = create_engine("sqlite://database.sqlite", echo=True, future=True)
