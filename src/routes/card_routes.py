from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from sqlalchemy.orm import Session

from dtos.card_dtos import CardRegisterRequestDTO
from controllers.card_controller import suggestedCardsByUser

router = APIRouter(prefix="/api/v1/cards", tags=["Cards module"])

@router.post("/", status_code=201)
def register(req: CardRegisterRequestDTO, db: Session = Depends(get_db)):
    return {
        "message": "to imple"
    }

@router.get("/suggested-cards-by-user/{user_id}")
def suggested_cards_by_user(user_id: str, db: Session = Depends(get_db)):
    controller = suggestedCardsByUser(user_id, db)
    return controller

