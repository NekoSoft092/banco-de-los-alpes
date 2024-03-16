from dtos.request_dtos import Step1RequestDTO, Step1ResponseDTO
from repositories.request_repository import RequestRepository
from sqlalchemy.orm import Session

def registrerRequestController(data: Step1RequestDTO, db, Session):
    rp = RequestRepository()
    rp.save(db, data)
    return Step1ResponseDTO(
        state=data.state
    )