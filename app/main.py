from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import engine, SessionLocal
from app import models, schemas, crud
from app.sample_data import insert_sample_data
import json

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
def startup_event():
    insert_sample_data()

@app.post("/screen/create", response_model=schemas.ScreenOut)
def create_screen(screen: schemas.ScreenCreate, db: Session = Depends(get_db)):
    screen_obj = models.Screen(
        name=screen.name,
        criteria=json.dumps(screen.criteria)
    )
    db.add(screen_obj)
    db.commit()
    db.refresh(screen_obj)

    return {
        "id": screen_obj.id,
        "name": screen_obj.name,
        "criteria": screen.criteria  
    }


@app.get("/screen/{screen_name}/run", response_model=list[schemas.StockOut])
def run_screen(screen_name: str, db: Session = Depends(get_db)):
    screen = crud.get_screen_by_name(db, screen_name)
    if not screen:
        raise HTTPException(status_code=404, detail="Screen not found")
    return crud.run_screen(db, screen)
