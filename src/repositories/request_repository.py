from sqlalchemy import insert
from schemas.request_schema import RequestSchema
from dtos.request_dtos import Step1RequestDTO
from sqlalchemy import Session

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