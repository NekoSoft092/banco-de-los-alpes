from sqlalchemy import insert
from schemas.user_schema import UserSchema
from dtos.auth_dtos import UserRegisterRequestDTO 
from sqlalchemy.orm import Session
from datetime import datetime

class UserRepository:

    @staticmethod
    def save (db: Session, data: UserRegisterRequestDTO) -> None:
        stmp = insert(UserSchema).values(
            identification_type = data.tipo_identificacion,
            identification_number = data.numero_identificacion,
            residence_address = data.direccion,
            # birth_date = datetime(data.fecha_nacimiento), 
            name = data.nombres,
            email = data.email, 
            nationality = data.nacionalidad, 
            profession = data.profesion, 
            #credit_score 
            is_client = data.es_cliente 
        )

        if(db):
            db.execute(stmp)
            db.commit()
        else:
            print('not session provided')
    
    @staticmethod
    def getById(db: Session, id: str):
        items = db.query(UserSchema).filter_by(id = id).all()
        return items
    
    @staticmethod
    def getByEmail(db: Session, email: str):
        items = db.query(UserSchema).filter_by(email = email).all()
        return items
        
    def update(self):
        print('to do')

    def delete(self):
        print('to do')
