import fitz
import logging
from app.core.exceptions import FileValidationException

logger = logging.getLogger(__name__)
def resume_converter(resume:bytes)->str:
    try:
        resume_file=fitz.open(stream=resume,filetype="pdf")
        extracted_text=""
        for page in resume_file:
            extracted_text+=page.get_text()
        resume_file.close()
        if not extracted_text.strip():
            raise FileValidationException(
                detail="Resume content is empty"
            )
        return extracted_text
    except FileValidationException:
        raise
    except Exception:
        logger.exception("PDF parsing failed")
        raise FileValidationException(
            detail="Invalid PDF file"
        )

