from fastapi import FastAPI, Depends, Request
import Model
from Database import SessionLocal_jobs,SessionLocal_apps, engine_jobs,engine_apps
from pydantic import BaseModel
from Model import Jobs, Candidate, Application
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates


job = FastAPI()

templates=Jinja2Templates(directory="templates")

@job.get("/")
def homepage(request:Request):
        return templates.TemplateResponse("Main.html",{
        "request":request})

@job.get("/recruiter")
def recpage(request:Request):
        return templates.TemplateResponse("home.html",{
        "request":request})



Model.Base.metadata.create_all(bind=engine_apps)
Model.Base.metadata.create_all(bind=engine_jobs)

class JobDetails(BaseModel):
    Job_ID: int
    Posted_by: str
    Job_Type: str
    Company: str
    Job_Location: str
    Is_Active: str


class ApplicationData(BaseModel):
    Cand_ID: int
    Job_ID: int
    First_Name: str
    Last_Name:str
    Ph_no:int
    Experience:int


def get_dbjobs():
    try:
        db = SessionLocal_jobs()
        yield db
    finally:
        db.close()

def get_dbapps():
    try:
        db = SessionLocal_apps()
        yield db
    finally:
        db.close()        

@job.get("/candidate")
async def can_job(request: Request, db: Session = Depends(get_dbjobs)):
    data = db.query(Jobs).all()
    return templates.TemplateResponse("Candidate.html",{
        "request":request,"data":data}) 


@job.get("/recruiter/job/{ID}")
async def job_dataid(request: Request, ID: int, db: Session = Depends(get_dbjobs)):
    data = db.query(Jobs).filter(Jobs.Job_ID == ID).all()
    return templates.TemplateResponse("home.html",{
        "request":request,"data":data})    


@job.get("/recruiter/jobs")
async def job_data(request: Request, db: Session = Depends(get_dbjobs)):
    data = db.query(Jobs).all()
    return templates.TemplateResponse("home.html",{
        "request":request,"data":data}) 


@job.post("/recruiter/jobs")
async def create_job(detail_request: JobDetails, db: Session = Depends(get_dbjobs)):

    post = Jobs()
    post.Job_ID = detail_request.Job_ID
    post.Is_Active=detail_request.Is_Active
    post.Posted_by=detail_request.Posted_by
    post.Company=detail_request.Company
    post.Job_Location=detail_request.Job_Location
    post.Job_Type=detail_request.Job_Type
    db.add(post)
    db.commit()
    return {
        "code": "success",
        "message": "job was added to the database"
    }    


@job.delete("/recruiter/jobs/{ID}")
async def job_databyID(request: Request, ID:int, db: Session = Depends(get_dbjobs)):
   
    db.query(Jobs).filter(Jobs.Job_ID == ID).delete()
    db.commit()
    data=db.query(Jobs).all()
    return {
        "code": "success",
        "message": "job was deleted from the database"} 


@job.post("/candidate/job/{ID}/apply")
async def create_application(detail_request: ApplicationData, ID:int, db: Session = Depends(get_dbapps)):

    application = Application()
    # application.Appl_ID = detail_request.Appl_ID
    application.Job_ID=ID
    application.Cand_ID = detail_request.Cand_ID
    application.First_Name = detail_request.First_Name
    application.Last_Name = detail_request.Last_Name
    application.Ph_no = detail_request.Ph_no
    application.Experience = detail_request.Experience


    db.add(application)
    db.commit()

    return {
        "code": "success",
        "message": "Application has been added to the database"
    }
