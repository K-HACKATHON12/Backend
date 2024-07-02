from typing import List
from models.population import PopulationWorkplace
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

@ctrl_router.get("/expenditure/1", response_model=List[ExpenditureSummary])
def expenditure(db: Session = Depends(get_db)):
    quarters = [20191, 20192, 20193, 20194, 20201, 20202, 20203, 20204, 20211, 20212, 20213, 20214, 20221, 20222, 20223, 20224, 20231, 20232, 20233, 20234]
    expenditure = db.query(
        CommercialExpenditure.STDR_YYQU_CD,
        func.sum(CommercialExpenditure.EXPNDTR_TOTAMT).label('total_amount')
    ).filter(
        CommercialExpenditure.STDR_YYQU_CD.in_(quarters)
    ).group_by(
        CommercialExpenditure.STDR_YYQU_CD
    ).order_by(
        CommercialExpenditure.STDR_YYQU_CD
    ).all()
    if not expenditure:
        raise HTTPException(status_code=404, detail="Expenditure not found")

    return expenditure