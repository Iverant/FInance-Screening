from pydantic import BaseModel
from typing import Dict, Any
from datetime import date

class StockOut(BaseModel):
    symbol: str
    name: str
    market_cap: float
    pe_ratio: float
    revenue: float
    date: date

    class Config:
        orm_mode = True

class ScreenCreate(BaseModel):
    name: str
    criteria: Dict[str, Dict[str, Any]]

class ScreenOut(BaseModel):
    id: int
    name: str
    criteria: Dict[str, Dict[str, Any]]

    class Config:
        orm_mode = True