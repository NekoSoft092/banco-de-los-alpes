from dtos.auth_dtos import UserRegisterRequestDTO, UserRegisterResponseDTO
from repositories.user_repository import UserRepository
from sqlalchemy.orm import Session

def registerUserController(data: UserRegisterRequestDTO, db: Session):
    rp = UserRepository()
    rp.save(db, data)
    return UserRegisterResponseDTO(
        nombre=data.nombres
    )