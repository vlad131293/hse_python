from pydantic import BaseModel
from typing import Optional


class Item(BaseModel):
    year: Optional[int]
    month: Optional[int]
    salary: Optional[float]
