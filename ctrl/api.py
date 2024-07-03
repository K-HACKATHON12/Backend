from typing import List
from models.population import PopulationWorkplace, PopulationStreet, PopulationResident
from models.location import LocApartmentInfo
from models.schema.population import PopulationWorkplacePydantic
from models.commercial import CommercialExpenditure
from models.schema.commercial import CommercialExpenditurePydantic
from db_config import get_db
from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy import func
from pydantic import BaseModel

ctrl_router = APIRouter()

@ctrl_router.get("/", response_model=List[PopulationWorkplacePydantic])
def population_workplace(db: Session = Depends(get_db)):
    population = db.query(PopulationWorkplace).limit(100).all()
    if not population:
        raise HTTPException(status_code=404, detail="Population not found")
    return population

@ctrl_router.get("/len", response_model=int)
def population_workplace_len(db: Session = Depends(get_db)):
    population = db.query(PopulationWorkplace).limit(100).all()
    if not population:
        raise HTTPException(status_code=404, detail="Population not found")
    return len(population)


class ExpenditureSummary(BaseModel):
    STDR_YYQU_CD: int
    total_amount: float

    class Config:
        orm_mode = True

@ctrl_router.get("/expenditure/{query}", response_model=List[ExpenditureSummary])
def expenditure(query: str, db: Session = Depends(get_db)):
    queryType = None
    if query == 'total':
        queryType = CommercialExpenditure.EXPNDTR_TOTAMT
    if query == 'lsr':
        queryType = CommercialExpenditure.LSR_EXPNDTR_TOTAMT
    if query == 'mcp':
        queryType = CommercialExpenditure.MCP_EXPNDTR_TOTAMT
    if query == 'plesr':
        queryType = CommercialExpenditure.PLESR_EXPNDTR_TOTAMT
    if query == 'edc':
        queryType = CommercialExpenditure.EDC_EXPNDTR_TOTAMT
    if query == 'cltur':
        queryType = CommercialExpenditure.CLTUR_EXPNDTR_TOTAMT

    if queryType is None:
        raise HTTPException(status_code=404, detail="Query not found")

    expenditure = db.query(
        CommercialExpenditure.STDR_YYQU_CD,
        func.sum(queryType).label('total_amount')
    ).group_by(
        CommercialExpenditure.STDR_YYQU_CD
    ).order_by(
        CommercialExpenditure.STDR_YYQU_CD
    ).all()
    if not expenditure:
        raise HTTPException(status_code=404, detail="Expenditure not found")

    return expenditure

class PopulationSummary(BaseModel):
    STDR_YYQU_CD: int
    total_population: int

    class Config:
        orm_mode = True

@ctrl_router.get("/pop/{query}", response_model=List[PopulationSummary])
def pop_street(query: str, db: Session = Depends(get_db)):

    queryType = None
    queryMound = None
    if query == 'res':
        queryType = PopulationResident
        queryMound = PopulationResident.TOT_REPOP_CO
    if query == 'wrk':
        queryType = PopulationWorkplace
        queryMound = PopulationWorkplace.TOT_WRC_POPLTN_CO
    if query == 'street':
        queryType = PopulationStreet
        queryMound = PopulationStreet.TOT_FLPOP_CO
    if query == 'apartment':
        queryType = LocApartmentInfo
        queryMound = LocApartmentInfo.APT_HSMP_CO

    if not queryType or not queryMound:
        raise HTTPException(status_code=404, detail="Query not found")

    population = db.query(
        queryType.STDR_YYQU_CD,
        func.sum(queryMound).label('total_population')
    ).group_by(
        queryType.STDR_YYQU_CD
    ).order_by(
        queryType.STDR_YYQU_CD
    ).all()
    if not population:
        raise HTTPException(status_code=404, detail="Population not found")
    return population

