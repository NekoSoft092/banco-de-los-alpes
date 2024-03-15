from database import Base
from sqlalchemy import String, Date, Integer, Boolean
from sqlalchemy.sql.schema import Column
from sqlalchemy.dialects.postgresql import UUID
import uuid


class UserSchema(Base):
    __tablename__ = 'users'

    id = Column(UUID( as_uuid=True), primary_key=True, default=uuid.uuid4)

    identification_type = Column(String, nullable = False)
    identification_number = Column(String, nullable=False)
    name = Column(String, nullable = False)
    residence_address = Column(String, nullable = True)
    birth_date = Column(Date, nullable = True)
    email = Column(String, nullable = False)
    nationality = Column(String, nullable = False)
    profession = Column(String, nullable = True)
    credit_score = Column(Integer, nullable = True)
    is_client = Column(Boolean, nullable = False)