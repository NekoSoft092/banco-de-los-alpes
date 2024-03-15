from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import os
from dotenv import load_dotenv
load_dotenv()

database_user: str | None = os.getenv('POSTGRESQL_USER')
database_host: str | None = os.getenv('POSTGRESQL_HOST')
database_port: str | None = os.getenv('POSTGRESQL_PORT')
database_password: str | None = os.getenv('POSTGRESQL_PASSWORD')
database_name: str | None = os.getenv('DATABASE_NAME')




SQLALCHEMY_DATABASE_URL = f'postgresql://{database_user}:{database_password}@{database_host}:{database_port}/{database_name}'


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
metadata = Base.metadata # type: ignore

def get_db():
    db = SessionLocal()
    try: 
        yield db
    except:
        db.close()

