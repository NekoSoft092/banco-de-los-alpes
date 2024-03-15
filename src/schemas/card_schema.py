from database import Base
from sqlalchemy.sql.schema import Column
from sqlalchemy import String, Integer, Date, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from schemas.user_schema import UserSchema

class CardSchema(Base):
    __tablename__ = 'cards'

    number = Column(String, primary_key = True)
    code_security = Column(Integer, nullable = False)
    expedition_date = Column(Date, nullable = False)
    expiration_year = Column(Integer, nullable = False)
    expiration_month = Column(Integer, nullable = False)
    amount = Column(Float, nullable = False)
    current = Column(String, nullable = False)

    user_id = Column(UUID, ForeignKey(UserSchema.id, ondelete='CASCADE'), nullable=True, unique=True)
    user = relationship('UserSchema', backref='card')
