from fastapi import UploadFile
from app.core.settings import settings
from app.core.exceptions import FileValidationException


ALLOWED_TYPES = ["application/pdf"]


async def validate_resume_file(file: UploadFile):

    if file.content_type not in ALLOWED_TYPES:
        raise FileValidationException(
            detail="Only PDF files are allowed"
        )

    content = await file.read()

    if len(content) > settings.MAX_FILE_SIZE:
        raise FileValidationException(
            detail="File size exceeded"
        )

    await file.seek(0)