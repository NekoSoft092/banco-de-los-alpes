from pydantic import BaseModel, EmailStr

class DocumentRegisterRequestDTO(BaseModel):
    id_review: str
    id_request: str
    state: str
    title: str
    is_valid: bool
    url: str

class DocumentRegisterResponseDTO(BaseModel):
    sended: bool
    title: str