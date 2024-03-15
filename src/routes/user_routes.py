from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session
from sqlalchemy import exc
from database import get_db

router = APIRouter(prefix="/v1/users", tags=["Users module"])


