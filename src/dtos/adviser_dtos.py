from pydantic import BaseModel, EmailStr

# Login
class AdviserLoginRequestDTO(BaseModel):
    email: EmailStr
    password: str

class AdviserLoginResponseDTO(BaseModel):
    token: str
    expires_on: int # milisegundos

# Register
class AdviserRegisterRequestDTO(BaseModel):
    nombre: str
    rol: str
    password: str
    email: EmailStr

class AdviserRegisterResponseDTO(BaseModel):
    token: str
    expires_on: int # milisegundos

# Recover password
class AdviserRecoverPasswordRequestDTO(BaseModel):
    email: str

class AdviserRecoverPasswordResponseDTO(BaseModel):
    sended: bool

# Change password
class AdviserChangePasswordRequestDTO(BaseModel):
    email: str
    code: str
    new_password: str

class AdviserChangePasswordResponseDTO(BaseModel):
    changed: bool