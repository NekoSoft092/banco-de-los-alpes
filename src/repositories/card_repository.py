from sqlalchemy import insert
from schemas.card_schema import CardSchema
from dtos.card_dtos import CardRegisterDTO
from sqlalchemy.orm import Session

class CardRepository:

    @staticmethod
    def save (db: Session, data: CardRegisterDTO) -> None:
        stmp = insert(CardSchema).values(
            number = data.number,
            code_security = data.code_security,
            expedition_date = data.expedition_date,
            expiration_year = data.expiration_year,
            expiration_month = data.expiration_month,
            amount = data.amount,
            curret = data.current,

            user_id = data.user_id
        )

        if(db):
            db.execute(stmp)
            db.commit()
        else:
            print('not session provided')
    
    @staticmethod
    def getById(db: Session, id: str):
        # items = db.query(UserSchema).filter_by(id = id).all()
        return 
    
    @staticmethod
    def getByEmail(db: Session, email: str):
        # items = db.query(UserSchema).filter_by(email = email).all()
        return
    
    @staticmethod
    def update(self):
        print('to do')
        return

    @staticmethod
    def delete(self):
        print('to do')
        return
