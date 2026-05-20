
from fastapi import APIRouter,File,UploadFile,Depends
from app.api.routes import service
from app.utils import validator,response_handler
from app.utils.response_handler import success_response
from app.core.limiter import  limiter
from fastapi import Request
router=APIRouter(
    prefix="/resume",
    tags=["Resume Analyzer"]
)

@router.post("/analyze")
@limiter.limit("5/minute")
async def analyze_resume(request:Request, file:UploadFile=File(...)):
    response = await service.ResumeService.resume_evaluation_ai(file)
    return success_response(
        data=response,
        message="Resume analyzed successfully"
    )