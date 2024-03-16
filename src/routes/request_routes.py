from fastapi import APIRouter, Depends, HTTPException
from dtos.request_dtos import Step1RequestDTO, Step1ResponseDTO

from sqlalchemy.orm import Session
from database import get_db
from controllers.request_controller import requestController

router = APIRouter(prefix="/api/v1/requests", tags=["Requests module"])

# Paso 1
@router.post("/step-1", status_code=201)
def step1(data: Step1RequestDTO, db: Session = Depends(get_db)):    
    controller: Step1ResponseDTO = requestController(data, db)
    return controller

