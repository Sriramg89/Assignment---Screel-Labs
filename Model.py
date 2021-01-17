from sqlalchemy import Boolean, Column, ForeignKey, Numeric, Integer, String
from sqlalchemy.orm import relationship

from Database import Base


class Jobs(Base):
    __tablename__ = "Jobs"

    Job_ID = Column(Integer, primary_key=True)
    Posted_by = Column(String)
    Job_Type = Column(String)
    Company = Column(String)
    Job_Location = Column(String)
    Is_Active = Column(String)


class Candidate(Base):
    __tablename__ = "Candidate"

    Cand_ID = Column(Integer, primary_key=True)
    First_Name = Column(String)
    Last_Name = Column(String)
    Ph_no = Column(Integer)
    Experience = Column(Integer)


class Application(Base):
    __tablename__ = "Application"

    Cand_ID = Column(Integer)
    Job_ID = Column(Integer, primary_key=True)
    First_Name = Column(String)
    Last_Name = Column(String)
    Ph_no = Column(Integer)
    Experience = Column(Integer)




