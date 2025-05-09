from app.database import SessionLocal
from app.models import Stock
from datetime import date

def insert_sample_data():
    db = SessionLocal()
    if db.query(Stock).count() == 0:
        stocks = [
            Stock(symbol="TCS", name="Tata Consultancy Services", market_cap=1300000, pe_ratio=28.5, revenue=160000, date=date(2023, 12, 31)),
            Stock(symbol="INFY", name="Infosys", market_cap=900000, pe_ratio=24.0, revenue=120000, date=date(2023, 12, 31)),
            Stock(symbol="RELIANCE", name="Reliance Industries", market_cap=1600000, pe_ratio=18.0, revenue=700000, date=date(2023, 12, 31)),
            Stock(symbol="WIPRO", name="Wipro", market_cap=400000, pe_ratio=15.5, revenue=70000, date=date(2023, 12, 31)),
            Stock(symbol="HDFC", name="HDFC Bank", market_cap=800000, pe_ratio=20.0, revenue=150000, date=date(2023, 12, 31)),
        ]
        db.bulk_save_objects(stocks)
        db.commit()
    db.close()
