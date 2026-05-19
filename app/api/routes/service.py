import logging
from fastapi import APIRouter,File,UploadFile
from app.AI.resume_converter import resume_converter
from app.AI.ai_resume_evaluater import ResumeEvaluator
from app.AI.ai_promptbuilder import set_resume_validation_prompt

logger = logging.getLogger(__name__)
class ResumeService:
    @staticmethod
    async def resume_evaluation_ai(file:UploadFile):
        try:
            if file.content_type!="application/pdf":
                logging.error("File type mismatch error identified")
                raise ValueError("File type mismatch")
            else:
                logger.info("Resume analysis started")
                file_bytes=await file.read()
                resume_content=resume_converter(file_bytes)
                prompt=set_resume_validation_prompt(resume_content)
                response=await ResumeEvaluator.resume_evaluator(prompt)
                logger.info("Resume analysis completed")
                return response
        except Exception as e:
            logging.error(f"Service processing failed. {e}")
            raise ValueError(" Service processing failed")