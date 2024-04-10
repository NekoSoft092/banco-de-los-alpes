from dtos.request_dtos import Step1RequestDTO, Step1ResponseDTO
from sqlalchemy.orm import Session
from repositories.user_repository import UserRepository

from datetime import datetime, timedelta

def requestController(data: Step1RequestDTO, db: Session) -> Step1ResponseDTO:
  
  # crear usuarui
  #rp = UserRepository()
  # rp.save(db, data)
  
  # crear reque


  return Step1ResponseDTO(
    state='in progress',
    created_at= datetime.now(),
    updated_at=datetime.now(),
    expiration_date=datetime.now() +  timedelta(days=30), 
    step=1
  )