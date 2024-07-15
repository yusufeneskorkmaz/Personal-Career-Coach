from fastapi import FastAPI, File, UploadFile, Form
from src.PersonalCareerCoach.pipeline.career_analysis_pipeline import CareerAnalysisPipeline

app = FastAPI()
pipeline = CareerAnalysisPipeline()

@app.post("/analyze")
async def analyze_career(
    resume: UploadFile = File(...),
    job_description: str = Form(...),
    github_username: str = Form(...)
):
    resume_content = await resume.read()
    result = pipeline.run(resume_content, job_description, github_username)
    return result

@app.get("/")
async def root():
    return {"message": "Welcome to Personal Career Coach API"}