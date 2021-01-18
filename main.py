            # Main Python script where Fast API is used to make requests from database ( Using SQLite database ) 

# Importing  necessary Python modules like fastapi,pydantic,sqlalchemy etc.

from fastapi import FastAPI, Depends, Request
from sqlalchemy.sql.expression import null, select,join,outerjoin  # sqlalchemy is used to send SQL requests to databases 
import Model                                                       # and also helps in ORM mapping
from Database import SessionLocal, engine
from pydantic import BaseModel                                   # Pydantic is used to ceate objects called BaseModels (commonly used)
from Model import Jobs, Candidate, Application
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates


job = FastAPI()                                                           

templates=Jinja2Templates(directory="templates")                                  

@job.get("/")                                                              # GET request using FastAPI --> lands on Career homepage
def homepage(request:Request):
        return templates.TemplateResponse("Main.html",{
        "request":request})

@job.get("/recruiter")                                                     # GET request using FastAPI --> lands on Recruiter page  
def recpage(request:Request):                                              # Recruiter login is hardcoded (So used a button instead)
        return templates.TemplateResponse("home.html",{
        "request":request})



Model.Base.metadata.create_all(bind=engine)


class JobDetails(BaseModel):                                         # Created a 'JobDetails' BaseModel class specifying members and types.
    Job_ID: int                                                             
    Posted_by: str                                                          
    Job_Type: str
    Company: str
    Job_Location: str
    Immediate_Joining: str


class ApplicationData(BaseModel):                                      # Created an Application data class specifying members     
                                                                       # and types.
    Job_ID: int
    First_Name: str
    Last_Name: str
    Qualification: str
    Ph_no: int
    Experience_years: int


def get_db():                                                           # Function to create an instance of the database
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()        

@job.get("/candidate")                                                   # GET request using FastAPI --> lands on Candidate's page
async def can_job(request: Request, db: Session = Depends(get_db)):

    data=db.query(Jobs).outerjoin(Application,
     Jobs.Job_ID == Application.Job_ID).filter(Application.Job_ID == None)     #  Jobs that the candidate has already applied to 
                                                                               #  will not be shown (SQL join and filter used)
    return templates.TemplateResponse("Candidate.html",{
        "request":request,"data":data}) 


@job.get("/recruiter/job/{ID}")                                                # GET request to get a job post by ID
async def job_dataid(request: Request, ID: int, 
db: Session = Depends(get_db)):
    data = db.query(Jobs).filter(Jobs.Job_ID == ID).all()
    return templates.TemplateResponse("home.html",{
        "request":request,"data":data})    


@job.get("/recruiter/jobs")                                                     # GET request to view all job posts        
async def job_data(request: Request, db: Session = Depends(get_db)):
    data = db.query(Jobs).all()
    return templates.TemplateResponse("home.html",{
        "request":request,"data":data}) 


@job.post("/recruiter/jobs")                                                    # POST request to add a job post.         
async def create_job(detail_request: JobDetails,                                # It gets added to SQLite Database as well.
db: Session = Depends(get_db)):

    post = Jobs()                                                               # Creates an instance of Jobs class to help assign values
    post.Job_ID = detail_request.Job_ID                                         # to data members
    post.Immediate_Joining=detail_request.Immediate_Joining
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


@job.delete("/recruiter/jobs/{ID}")                                             # DELETE request to remove an entry from the database  
async def job_databyID(request: Request, ID:int,                                # based on ID provided
db: Session = Depends(get_db)):
   
    db.query(Jobs).filter(Jobs.Job_ID == ID).delete()
    db.commit()
    data=db.query(Jobs).all()
    return {
        "code": "success",
        "message": "job was deleted from the database"} 


@job.post("/candidate/job/{ID}/apply")                                      # POST request for candidate to apply for a particular job
async def create_application(detail_request: ApplicationData,
 ID:int, db: Session = Depends(get_db)):

    application = Application()
    application.Job_ID=ID
    application.Qualification = detail_request.Qualification
    application.First_Name = detail_request.First_Name
    application.Last_Name = detail_request.Last_Name
    application.Ph_no = detail_request.Ph_no
    application.Experience_years = detail_request.Experience_years


    db.add(application)                                                     # Adding details to the database and commiting the changes
    db.commit()

    return {                                                                # Alert message to inform the user that action was sucessful
        "code": "success",
        "message": "Application has been added to the database"
    }
