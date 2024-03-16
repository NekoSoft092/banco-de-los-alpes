from fastapi import APIRouter, Depends, HTTPException
from dtos.request_dtos import Step1RequestDTO

from sqlalchemy.orm import Session
from sqlalchemy import exc
from database import get_db

router = APIRouter(prefix="/v1/resquests", tags=["Requests module"])

# Paso 1
@router.post("/", status_code=201)
def step1(data: Step1RequestDTO, db: Session = Depends(get_db)):
    # To implement
    return 