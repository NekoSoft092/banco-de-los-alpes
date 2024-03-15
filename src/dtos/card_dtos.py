from pydantic import BaseModel
import datetime

# Register
class CardRegisterRequestDTO(BaseModel):
    user_id: str
    amount: float
    current: str

class CardRegisterResponseDTO(BaseModel):
    number: str
    expedition_date: str
    expiration_year: int
    expiration_month: int
    amount: float
    current: str

class CardRegisterDTO:
    number: str
    code_security: int
    expedition_date: datetime
    expiration_year: int
    expiration_month: int 
    amount: float
    current: str
    user_id: str
