from fastapi import FastAPI

from model_data import Item
from backend import WorkDays


app = FastAPI(
    title='hourly-wage-rate'
)
model = WorkDays()


@app.post("/accept_data")
async def accept_data(data: Item):
    result = model.main(dict(data))
    return result
