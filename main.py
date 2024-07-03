from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ctrl.api import ctrl_router
from chat.api import langchain_router

app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 도메인에서의 접근을 허용합니다. 보안상 필요한 도메인만 허용하는 것이 좋습니다.
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메소드를 허용합니다.
    allow_headers=["*"],  # 모든 HTTP 헤더를 허용합니다.
)

app.include_router(langchain_router, prefix="/chat")
app.include_router(ctrl_router, prefix="/query")

