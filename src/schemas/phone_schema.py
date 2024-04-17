from database import Base
from sqlalchemy.sql.schema import Column
from sqlalchemy import String, Integer, Date, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from schemas.user_schema import UserSchema

class PhoneSchema(Base):
    __tablename__ = 'phones'

    id = Column(UUID, primary_key=True, nullable=False)
    code_country = Column(String, nullable=False)
    number = Column(String, nullable=False)

    user_id = Column(UUID, ForeignKey(UserSchema.id, ondelete='CASCADE'), 
                     nullable=True, unique=True)
    user = relationship('UserSchema', backref='phone')