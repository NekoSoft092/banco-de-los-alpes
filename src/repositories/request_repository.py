from sqlalchemy import insert
from schemas.request_schema import RequestSchema
from dtos.request_dtos import Step1RequestDTO
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError 

class RequestRepository:

    @staticmethod
    def save(db: Session, data: Step1RequestDTO) -> None:
        stmp = insert(RequestSchema).values(
            status=data.status,
            creation_date=data.creation_date,
            last_modification=data.last_modification,
            expiration_date=data.expiration_date,
            step=data.step,

            user_id =data.user_id,
            card_id=data.card_id
        )

        if(db):
            db.execute(stmp)
            db.commit()
        else:
            print('not session provided')

    @staticmethod
    def find_by_id(db: Session, request_id: int) -> RequestSchema:
        try:
            return db.query(RequestSchema).filter(RequestSchema.id == request_id).first()
        except SQLAlchemyError as e:
            print(f"An error occurred while fetching request: {str(e)}")
            return None