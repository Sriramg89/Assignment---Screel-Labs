from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL_JOBS = "sqlite:///./joblist.db"
SQLALCHEMY_DATABASE_URL_APPS = "sqlite:///./applist.db"

engine_jobs = create_engine(
    SQLALCHEMY_DATABASE_URL_JOBS, connect_args={"check_same_thread": False}
)

engine_apps = create_engine(
    SQLALCHEMY_DATABASE_URL_APPS, connect_args={"check_same_thread": False}
)

SessionLocal_jobs = sessionmaker(autocommit=False, autoflush=False, bind=engine_jobs)
SessionLocal_apps = sessionmaker(autocommit=False, autoflush=False, bind=engine_apps)

Base = declarative_base()




