from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.merchant_data import MerchantData, MerchantDataCreate
from app.crud.crud_merchant_data import get_merchant_data, get_all_merchant_data, create_merchant_data, update_merchant_data, delete_merchant_data
from app.db.session import get_db

router = APIRouter()

@router.post("/", response_model=MerchantData)
def create_new_merchant_data(merchant_data: MerchantDataCreate, db: Session = Depends(get_db)):
    return create_merchant_data(db=db, merchant_data=merchant_data)

@router.get("/{trdar_cd}", response_model=MerchantData)
def read_merchant_data(trdar_cd: str, db: Session = Depends(get_db)):
    db_merchant_data = get_merchant_data(db, trdar_cd)
    if not db_merchant_data:
        raise HTTPException(status_code=404, detail="Merchant data not found")
    return db_merchant_data

@router.get("/", response_model=list[MerchantData])
def read_all_merchant_data(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_all_merchant_data(db, skip=skip, limit=limit)

@router.put("/{trdar_cd}", response_model=MerchantData)
def update_existing_merchant_data(trdar_cd: str, updates: MerchantDataCreate, db: Session = Depends(get_db)):
    updated_merchant_data = update_merchant_data(db, trdar_cd, updates)
    if not updated_merchant_data:
        raise HTTPException(status_code=404, detail="Merchant data not found")
    return updated_merchant_data

@router.delete("/{trdar_cd}", response_model=bool)
def delete_existing_merchant_data(trdar_cd: str, db: Session = Depends(get_db)):
    success = delete_merchant_data(db, trdar_cd)
    if not success:
        raise HTTPException(status_code=404, detail="Merchant data not found")
    return success
