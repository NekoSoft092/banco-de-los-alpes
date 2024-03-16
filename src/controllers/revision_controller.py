from dtos.review_dtos import ReviewRegisterRequestDTO, ReviewRegisterResponseDTO
from repositories.revision_repository import revisionRepository
from sqlalchemy.orm import Session
from datetime import datetime

def revisionRegisterController(data: ReviewRegisterRequestDTO, db: Session):
    rp = revisionRepository()
    rp.save(db, data)
    fecha = datetime.now()
    return ReviewRegisterResponseDTO(
        id_request=data.id_request,
        title=data.title,
        annotation=data.annotation,
        revision_date=fecha
    )
  