from fastapi import APIRouter, HTTPException
from app.services.langchain_service import get_capital

router = APIRouter()

@router.get("/capital/{country}")
def read_capital(country: str):
    response = get_capital(country)
    if "error" in response.lower():
        raise HTTPException(status_code=500, detail=response)
    return {"country": country, "capital": response}
