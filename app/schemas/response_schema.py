from pydantic import BaseModel,Field,EmailStr
import types

class ResumeResponse(BaseModel):
    name:str=Field(min_length=2, max_length=100)
    phone:str
    email:EmailStr
    skills:list[str]
    score:int=Field(ge=1, le=10)
    feedback:str=Field(max_length=500)
