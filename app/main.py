from fastapi import FastAPI, Depends
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List
from models import SalesData
from schemas import SalesSummary, SalesRequestParams
from database import get_db

app = FastAPI()

# Endpoint to get top 5 regions by total sales
@app.post("/top-regions", response_model=List[SalesSummary])
async def get_top_regions(params: SalesRequestParams, db: Session = Depends(get_db)):
    query = (
        select(
            SalesData.region,
            func.sum(SalesData.sales_amount).label('total_sales')
        )
        .filter(
            SalesData.sales_date >= params.start_date,
            SalesData.sales_date <= params.end_date,
            SalesData.product_category == params.product_category
        )
        .group_by(SalesData.region)
        .order_by(func.sum(SalesData.sales_amount).desc())
        .limit(5)
    )

    result = await db.execute(query)
    top_regions = result.fetchall()

    summary = [
        SalesSummary(region=row[0], total_sales=float(row[1])) for row in top_regions
    ]

    return summary