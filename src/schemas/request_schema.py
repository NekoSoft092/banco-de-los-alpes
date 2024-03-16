from database import Base
from sqlalchemy.sql.schema import Column
from sqlalchemy import String, Integer, Date, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from schemas.card_schema import CardSchema
from schemas.user_schema import UserSchema

class RequesSchema(Base):
    __tablename__ = 'requests'

    status = Column(String, nullable = False)
    creation_date = Column(Date, nullable = False)
    last_modification = Column(Date, nullable = False)
    expiration_date = Column(Date, nullable = False)
    step = Column(Integer, nullable = False)

    card_id = Column(UUID, ForeignKey(CardSchema.number, ondelete='CASCADE'),
                     nullable=True, unique=False)
    card = relationship('CardSchema', backref='request')

    user_id = Column(UUID, ForeignKey(UserSchema.id, ondelete='CASCADE'), 
                     nullable=True, unique=True)
    user = relationship('UserSchema', backref='request')

