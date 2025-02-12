from pydantic import BaseModel, Field, ConfigDict
from datetime import date
from typing import Optional

class CardInfoUpdateSchema(BaseModel):
    card_name: Optional[str] = Field(None, max_length=50)
    bank: Optional[str] = Field(None, max_length=50)
    maxconsume: Optional[int] = None
    curramount: Optional[int] = None
    description: Optional[str] = None
    store: Optional[str] = None
    rewardstype: Optional[str] = None
    daterange_start: Optional[date] = None  # 會自動轉換成 date 格式
    daterange_end: Optional[date] = None
    postingdate: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)
