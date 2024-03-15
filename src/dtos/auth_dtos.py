from pydantic import BaseModel, EmailStr

class UserDTO(BaseModel):
    tipo_identificacion: str
    numero_identificacion: str
    nombre: str
    direccion: str
    fecha_nacimiento: str
    email: EmailStr
    nacionalidad: str
    profesion: str
    credit_score: int
    es_cliente: bool



