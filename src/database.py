from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import os

database_user: str | None = os.getenv('POSTGRESQL_USER')
database_host: str | None = os.getenv('POSTGRESQL_HOST')
database_port: str | None = os.getenv('POSTGRESQL_PORT')
database_password: str | None = os.getenv('POSTGRESQL_PASSWORD')
database_name: str | None = os.getenv('DATABASE_NAME')

SQLALCHEMY_DATABASE_URL: str = ''

# SQLALCHEMY_DATABASE_URL: str = 'postgresql://postgres:docker@localhost:5432/loy_db'
if(database_name != None and database_user != None and database_host != None and database_password != None and database_port != None):
    SQLALCHEMY_DATABASE_URL = 'postgresql://'+database_user+':'+database_password+'@'+database_host+':'+database_port+'/'+database_name
elif(database_name!= None):
    SQLALCHEMY_DATABASE_URL = "sqlite:///./"+database_name+".db"
else:
    print('Warning: no envs variables')

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

