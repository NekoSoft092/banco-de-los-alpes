from database import Base
from sqlalchemy import String, Date, Integer, Boolean
from sqlalchemy.sql.schema import Column
from sqlalchemy.dialects.postgresql import UUID
import uuid

class RevisionSchema(Base):
    __tablename__ = 'revisions'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    revision_date = Column(Date, nullable=False)
    anotations = Column(String, nullable=True)

    # request_id = Column(UUID(as_uuid=True), ForeignKey('requests.id'), nullable=False)