from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session
from sqlalchemy import exc
from database import get_db
from dtos.review_dtos import ReviewRegisterRequestDTO, ReviewRegisterResponseDTO
from controllers.revision_controller import revisionRegisterController

router= APIRouter(prefix="/v1/revisions", tags=["Revisions module"])

@router.post("/register", status_code=201)
def register(req: ReviewRegisterRequestDTO, db: Session = Depends(get_db)) -> ReviewRegisterResponseDTO:
    response: ReviewRegisterResponseDTO = revisionRegisterController(data=req,db= db)
    return response
