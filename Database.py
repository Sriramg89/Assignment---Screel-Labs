        # This Python script is used to create database engine and classes needed for SQL querying (Uses SQLAlchemy Python toolkit)  

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./joblist.db"                              # SQLite URL to create a database engine and sessions to
                                                                                # communicate with the database
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()                                                       # Creates a Base class for SQLAlchemy ORM usage 




