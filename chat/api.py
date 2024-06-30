from fastapi import APIRouter, HTTPException, Query
from chat.services.langchain_service import get_query

router = APIRouter()

@router.get("/")
def read_query(query: str = Query(..., description="Query string to find query")):
    response = get_query(query)
    if "error" in response.lower():
        raise HTTPException(status_code=500, detail=response)
    return {"query": query, "response": response}