# Python script to create model database tables needed.

from sqlalchemy import Boolean, Column, ForeignKey, Numeric, Integer, String
from sqlalchemy.orm import relationship

from Database import Base


class Jobs(Base):                                                                       # Creating a class Jobs of Base type
    __tablename__ = "Jobs"                                                              # with members to create instances later 
                                                                                        # using FastAPI. 
    Job_ID = Column(Integer, primary_key=True)
    Posted_by = Column(String)
    Job_Type = Column(String)
    Company = Column(String)
    Job_Location = Column(String)
    Immediate_Joining = Column(String)


class Candidate(Base):                                                                  # Creating a class Candidate with members
    __tablename__ = "Candidate"

    Cand_ID = Column(Integer, primary_key=True)
    First_Name = Column(String)
    Last_Name = Column(String)
    Ph_no = Column(Integer)
    Experience = Column(Integer)


class Application(Base):                                                            # Creating a class Application with members
    __tablename__ = "Application"

    Job_ID = Column(Integer, primary_key=True)
    First_Name = Column(String)
    Last_Name = Column(String)
    Qualification=Column(String)
    Ph_no = Column(Integer)
    Experience_years = Column(Integer)




