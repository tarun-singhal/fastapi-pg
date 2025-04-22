from pydantic import BaseModel
from typing import List
from datetime import datetime

class SalesSummary(BaseModel):
    region: str
    total_sales: float

class SalesRequestParams(BaseModel):
    start_date: datetime
    end_date: datetime
    product_category: str

    class Config:
        orm_mode = True