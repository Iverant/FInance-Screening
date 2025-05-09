from sqlalchemy.orm import Session
from app import models
import json


def create_screen(db: Session, name: str, criteria: dict):
    db_screen = models.Screen(name=name, criteria=json.dumps(criteria))
    db.add(db_screen)
    db.commit()
    db.refresh(db_screen)
    return db_screen

def get_screen_by_name(db: Session, name: str):
    return db.query(models.Screen).filter(models.Screen.name == name).first()

def run_screen(db: Session, screen: models.Screen):
    criteria = json.loads(screen.criteria)
    query = db.query(models.Stock)

    for field, condition in criteria.items():
        for op, value in condition.items():
            col = getattr(models.Stock, field)
            if op == "gt":
                query = query.filter(col > value)
            elif op == "lt":
                query = query.filter(col < value)
            elif op == "eq":
                query = query.filter(col == value)

    return query.all()