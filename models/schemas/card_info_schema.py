from pydantic import BaseModel, Field, ConfigDict
from datetime import date
from typing import Optional


class CardInfoSchema(BaseModel):
    card_id: int
    card_name: str = Field(..., max_length=50)
    bank: str = Field(..., max_length=50)
    maxconsume: Optional[int] = None
    curramount: Optional[int] = None
    description: Optional[str] = None
    store: Optional[str] = None
    rewardstype: Optional[str] = None
    daterange_start: Optional[date] = None
    daterange_end: Optional[date] = None
    postingdate: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)

