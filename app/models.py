from sqlalchemy import Column, String, Integer, Numeric, DateTime
from database import Base

class SalesData(Base):
    __tablename__ = 'sales_data'

    id = Column(Integer, primary_key=True, index=True)
    region = Column(String, index=True)
    product_category = Column(String)
    sales_amount = Column(Numeric)
    sales_date = Column(DateTime)