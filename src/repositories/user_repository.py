from sqlalchemy import insert
from schemas.user_schema import UserSchema
from dtos.auth_dtos import UserRegisterRequestDTO 
from sqlalchemy.orm import Session
from sqlalchemy.engine.cursor import LegacyCursorResult

from datetime import datetime


class UserRepository:

    @staticmethod
    def save (db: Session, data: UserRegisterRequestDTO) -> str:
        stmp = insert(UserSchema).values(
            identification_type = data.tipo_identificacion,
            identification_number = data.numero_identificacion,
            residence_address = data.direccion,
            # birth_date = datetime(data.fecha_nacimiento), 
            name = data.nombres,
            email = data.email, 
            nationality = data.nacionalidad, 
            profession = data.profesion, 
            credit_score = data.credit_score,
            is_client = data.es_cliente, 
            ingresos = data.ingresos
        )
        
        if(db):
            a: LegacyCursorResult = db.execute(stmp)
            print(a.inserted_primary_key.__str__())
            db.commit()
            return (a.inserted_primary_key.__str__())
        else:
            print('not session provided')
            return ''
    
    @staticmethod
    def getById(db: Session, id: str):

        items = db.query(UserSchema).filter_by(id = '06aa91cb-b4d4-44ce-bab8-45f87db3e30a').all()
        print(items)
        return items
    
    @staticmethod
    def getById(db: Session, id: str):
        # Utiliza el método get() para buscar por ID
        user = db.query(UserSchema).get(id)
        
        if user:
            print(user)  # Imprime el objeto encontrado (opcional)
            return user
        else:
            print(f"No se encontró ningún usuario con ID {id}")
            return None


        
    def update(self):
        print('to do')

    def delete(self):
        print('to do')
