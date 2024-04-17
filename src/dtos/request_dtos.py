from pydantic import BaseModel, EmailStr
from datetime import datetime 

# step 0 - login
class Step0RequestDTO(BaseModel):
    numero_celular: str
    indicativos: str

class Step0ResponseDTO(BaseModel):
    step: int

# step 1
class Step1RequestDTO(BaseModel):
    nombres: str
    apellidos: str
    ciudad: str
    numero_celular: str
    indicativo: str
    email: str
    nacionalidad: str

class Step1ResponseDTO(BaseModel):
    state: str
    created_at: datetime
    updated_at: datetime
    expiration_date: datetime
    step: int

# Step 2
class Step2RequestDTO(BaseModel):
    code: str

class Step2ResponseDTO(BaseModel):
    token: str
    step: int

# Step 3
class Step3PasivoDTO(BaseModel):
    concepto: str
    monto_base: int
    cuotas_restantes: int
    valor_mensual: int

class Step3ActivoDTO(BaseModel):
    concepto: str
    avaluo: int

class Step3RequestDTO(BaseModel):
    profesion: str
    nombre_actividad: str
    descripcion_actividad: str
    rut_code: str
    ingresos_mensuales: int

    pasivos: list[Step3PasivoDTO]

    activos: list[Step3ActivoDTO]

class Step3ResponseDTO(BaseModel):
    step: int
    cards_suggested: str

# Step 4
class Step4RequestDTO(BaseModel):
    id_card_accepted: str


