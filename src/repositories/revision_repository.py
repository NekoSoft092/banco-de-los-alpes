from sqlalchemy import insert
from schemas.revision_schema import RevisionSchema
from dtos.auth_dtos import UserRegisterRequestDTO 
from dtos.review_dtos import ReviewRegisterRequestDTO
from sqlalchemy.orm import Session
from datetime import datetime


class revisionRepository:
    @staticmethod
    def save (db: Session, data: UserRegisterRequestDTO) -> None:
        stmp = insert(RevisionSchema).values(ReviewRegisterRequestDTO,
        revision_date = data.revision_date,
        anotations = data.anotations
        )
        if(db):
            db.execute(stmp)
            db.commit()
        else:
            print('not session provided')

    @staticmethod
    def getById(db: Session, id: str):
        items = db.query(RevisionSchema).filter_by(id = id).all()
        return items
    
    @staticmethod
    def getByRequest(db: Session, request_id: str):
        items = db.query(RevisionSchema).filter_by(request_id = request_id).all()
        return items
    
    @staticmethod
    def getByTitle(db: Session, title: str):
        items = db.query(RevisionSchema).filter_by(title = title).all()
        return items
    
    def update(self):
        print('to do')

    def delete(self):
        print('to do')
