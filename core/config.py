import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

class Settings:
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")

settings = Settings()
