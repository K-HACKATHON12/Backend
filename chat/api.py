from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from chat.services.langchain_service import get_query

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]

langchain_router = APIRouter()

@langchain_router.post("/")
def read_query(chat_request: ChatRequest):
    response = get_query(chat_request.messages)
    if "error" in response.lower():
        raise HTTPException(status_code=500, detail=response)
    return {"response": response}
