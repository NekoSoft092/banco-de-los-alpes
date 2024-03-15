from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# register
class ReviewRegisterRequestDTO(BaseModel):
    email_adviser: str
    title: str
    annotations: Optional[str]

class ReviewRegisterResponseDTO(BaseModel):
    email_adviser: str
    title: str
    annotation: Optional[str]
    created_at: datetime

# delete 
class ReviewDeleteRequestDTO(BaseModel):
    id_review: str

class ReviewDeleteRequestDTO(BaseModel):
    deleted: bool