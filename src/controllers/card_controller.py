from dtos.auth_dtos import UserRegisterRequestDTO, UserRegisterResponseDTO
from repositories.user_repository import UserRepository
from sqlalchemy.orm import Session

def suggestedCardsByUser(user_id: str, db: Session):
    lista = [ {
            "numero": "1234 5678 9012 3456",
            "titular": "Juan Pérez",
            "fecha_expiracion": "12/25",
            "codigo_seguridad": "123",
            "tipo": "Visa",
            "cupo": 50000000  # El 
        },  {
            "numero": "1234 5678 9012 3456",
            "titular": "Juan Pérez",
            "fecha_expiracion": "12/25",
            "codigo_seguridad": "123",
            "tipo": "Visa",
            "cupo": 7000000  # El 
        }]
    rp = UserRepository()
    result = rp.getById(db, user_id)
    if result.ingresos < 1300000:
        return lista[0]

    return lista
