from pydantic import BaseModel, EmailStr
from datetime import datetime 

# step 1
class Step1RequestDTO(BaseModel):
    nombres: str
    apellidos: str
    ciudad: str
    numero_celular: str
    indicativo: str
    email: str

class Step1ResponseDTO(BaseModel):
    state: str
    created_at: datetime
    updated_at: datetime
    expiration_date: datetime
    step: int



