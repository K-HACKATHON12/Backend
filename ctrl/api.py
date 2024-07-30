from typing import List
from models.population import PopulationWorkplace, PopulationStreet, PopulationResident
from models.location import LocAdministrativeDistrict
from models.location import LocApartmentInfo
from models.schema.population import PopulationWorkplacePydantic
from models.commercial import CommercialExpenditure
from db_config import get_db
from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy import func
from pydantic import BaseModel
from pyproj import Transformer

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


class AgeGroupPopulation(BaseModel):
    male: int
    female: int
    total: int

class PopulationSummary(BaseModel):
    TRDAR_CD: int
    TRDAR_CD_NM: str
    TRDAR_SE_CD_NM: str
    STDR_YYQU_CD: int
    AGE_10: AgeGroupPopulation
    AGE_20: AgeGroupPopulation
    AGE_30: AgeGroupPopulation
    AGE_40: AgeGroupPopulation
    AGE_50: AgeGroupPopulation
    AGE_60_ABOVE: AgeGroupPopulation

    class Config:
        orm_mode = True

@ctrl_router.get("/pop/age/{trdar_cd}", response_model=List[PopulationSummary])
def pop_street(trdar_cd: int, db: Session = Depends(get_db)):
    population = db.query(PopulationResident).filter(
        PopulationResident.TRDAR_CD == trdar_cd,
        PopulationResident.STDR_YYQU_CD.between(20201, 20241)
    ).order_by(PopulationResident.STDR_YYQU_CD).all()

    if not population:
        raise HTTPException(status_code=404, detail="Population not found")

    result = [
        PopulationSummary(
            TRDAR_CD=item.TRDAR_CD,
            TRDAR_CD_NM=item.TRDAR_CD_NM,
            TRDAR_SE_CD_NM=item.TRDAR_SE_CD_NM,
            STDR_YYQU_CD=item.STDR_YYQU_CD,
            AGE_10=AgeGroupPopulation(
                male=item.MAG_10_REPOP_CO,
                female=item.FAG_10_REPOP_CO,
                total=item.AGRDE_10_REPOP_CO
            ),
            AGE_20=AgeGroupPopulation(
                male=item.MAG_20_REPOP_CO,
                female=item.FAG_20_REPOP_CO,
                total=item.AGRDE_20_REPOP_CO
            ),
            AGE_30=AgeGroupPopulation(
                male=item.MAG_30_REPOP_CO,
                female=item.FAG_30_REPOP_CO,
                total=item.AGRDE_30_REPOP_CO
            ),
            AGE_40=AgeGroupPopulation(
                male=item.MAG_40_REPOP_CO,
                female=item.FAG_40_REPOP_CO,
                total=item.AGRDE_40_REPOP_CO
            ),
            AGE_50=AgeGroupPopulation(
                male=item.MAG_50_REPOP_CO,
                female=item.FAG_50_REPOP_CO,
                total=item.AGRDE_50_REPOP_CO
            ),
            AGE_60_ABOVE=AgeGroupPopulation(
                male=item.MAG_60_ABOVE_REPOP_CO,
                female=item.FAG_60_ABOVE_REPOP_CO,
                total=item.AGRDE_60_ABOVE_REPOP_CO
            )
        )
        for item in population
    ]

    return result


class LocSummary(BaseModel):
    TRDAR_CD: int
    TRDAR_CD_NM: str
    longitude: float
    latitude: float

    class Config:
        orm_mode = True

@ctrl_router.get("/loc", response_model=List[LocSummary])
def loc_summary(db: Session = Depends(get_db)):
    population = db.query(LocAdministrativeDistrict).all()
    if not population:
        raise HTTPException(status_code=404, detail="Population not found")

    transformer = Transformer.from_crs("EPSG:5181", "EPSG:4326", always_xy=True)
    return [
        LocSummary(
            TRDAR_CD=item.TRDAR_CD,
            TRDAR_CD_NM=item.TRDAR_CD_NM,
            longitude=lon,
            latitude=lat
        )
        for item in population
        for lon, lat in [transformer.transform(item.XCNTS_VALUE, item.YDNTS_VALUE)]
    ]