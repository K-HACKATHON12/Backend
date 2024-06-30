from typing import List
from models.population import PopulationWorkplace
from models.schema.population import PopulationWorkplacePydantic
from db_config import get_db
from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter, HTTPException

ctrl_router = APIRouter()

@ctrl_router.get("/", response_model=List[PopulationWorkplacePydantic])
def read_facility_info(db: Session = Depends(get_db)):
    facility_info = db.query(PopulationWorkplace).limit(100).all()
    if not facility_info:
        raise HTTPException(status_code=404, detail="Facility not found")
    return facility_info

@ctrl_router.get("/len", response_model=int)
def len_info(db: Session = Depends(get_db)):
    facility_info = db.query(PopulationWorkplace).limit(100).all()
    if not facility_info:
        raise HTTPException(status_code=404, detail="Facility not found")
    return len(facility_info)