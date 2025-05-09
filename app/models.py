from sqlalchemy import Column, Integer, String, Float, Date
from app.database import Base

class Stock(Base):
    __tablename__ = "stocks"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, index=True)
    name = Column(String)
    market_cap = Column(Float)
    pe_ratio = Column(Float)
    revenue = Column(Float)
    date = Column(Date)

class Screen(Base):
    __tablename__ = "screens"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    criteria = Column(String)  # Stored as JSON string