from dtos.request_dtos import Step1RequestDTO
from sqlalchemy.orm import Session
from repositories.user_repository import UserRepository

def requestController(data: Step1RequestDTO, db: Session):
  rp = UserRepository()
  rp.save(db, data)