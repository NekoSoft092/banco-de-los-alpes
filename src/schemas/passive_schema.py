from database import Base
from sqlalchemy.sql.schema import Column
from sqlalchemy import String, Integer, Date, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from schemas.user_schema import UserSchema

class PassiveSchema(Base):
    __tablename__ = 'passives'

    id = Column(UUID, primary_key=True, nullable=False)

    concept = Column(String, nullable=False)
    amount = Column(Integer, nullable=False)
    remaining_installments = Column(Integer, nullable=False)
    fee_value = Column(Integer, nullable=False)
    
    user_id = Column(UUID, ForeignKey(UserSchema.id, ondelete='CASCADE'), 
                     nullable=True, unique=True)
    user = relationship('UserSchema', backref='passive')