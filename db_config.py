from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import dotenv_values
from urllib.parse import quote

# take environment variables from .env
config = dotenv_values("DB.env")

# URL 인코딩을 통해 특수 문자 처리
username = config['USERNAME']
password = quote(config['PASSWORD'])  # 비밀번호 인코딩
host = config['HOST']
port = config['PORT']
database = config['DATABASE']

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()