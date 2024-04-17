from database import Base
from sqlalchemy.sql.schema import Column
from sqlalchemy import String, Integer, Date, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from schemas.user_schema import UserSchema

class ActiveSchema(Base):
    __tablename__ = 'actives'

    id = Column(UUID, primary_key=True, nullable=False)
    concept = Column(String, nullable=False)
    appraisal = Column(Integer, nullable=False)

    user_id = Column(UUID, ForeignKey(UserSchema.id, ondelete='CASCADE'), 
                     nullable=True, unique=True)
    user = relationship('UserSchema', backref='active')