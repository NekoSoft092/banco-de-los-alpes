from pydantic import BaseModel, EmailStr
from typing import Optional

class UserRegisterRequestDTO(BaseModel):
    tipo_identificacion: str
    numero_identificacion: str
    nombres: str
    apellidos: str
    direccion: str
    fecha_nacimiento: str
    email: EmailStr
    nacionalidad: str
    profesion: str
    credit_score: Optional[int]
    es_cliente: bool



class UserRegisterResponseDTO(BaseModel):
    nombre: str