from fastapi import HTTPException

class FileValidationException(HTTPException):

    def __init__(self, detail: str):
        super().__init__(status_code=400, detail=detail)


class AIServiceException(HTTPException):

    def __init__(self, detail: str):
        super().__init__(status_code=500, detail=detail)


class SecretManagerException(HTTPException):

    def __init__(self, detail: str):
        super().__init__(status_code=500, detail=detail)