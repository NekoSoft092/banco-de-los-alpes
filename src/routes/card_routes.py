from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from sqlalchemy.orm import Session

from dtos.card_dtos import CardRegisterRequestDTO

router = APIRouter(prefix="/api/v1/cards", tags=["Cards module"])

@router.post("/", status_code=201)
def register(req: CardRegisterRequestDTO, db: Session = Depends(get_db)):
    return {
        "message": "to imple"
    }

