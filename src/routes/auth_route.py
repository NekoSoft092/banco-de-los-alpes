from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from sqlalchemy.orm import Session

from dtos.auth_dtos import UserRegisterRequestDTO, UserRegisterResponseDTO

from controllers.auth_controller import registerUserController

router = APIRouter(prefix="/api/v1/auth", tags=["Auth module"])

@router.post("/register", status_code=201)
def register(req: UserRegisterRequestDTO, db: Session = Depends(get_db)) -> UserRegisterResponseDTO:
    response: UserRegisterResponseDTO = registerUserController(data=req,db= db)
    return response

