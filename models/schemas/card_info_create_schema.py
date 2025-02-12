from pydantic import BaseModel, Field, ConfigDict
from datetime import date
from typing import Optional

class CardInfoCreateSchema(BaseModel):
    card_name: str = Field(..., max_length=50)
    bank: str = Field(..., max_length=50)
    maxconsume: Optional[int] = None
    curramount: Optional[int] = None
    description: Optional[str] = None
    store: Optional[str] = None
    rewardstype: Optional[str] = None
    daterange_start: Optional[date] = None  # 自動轉換日期格式
    daterange_end: Optional[date] = None  # 自動轉換日期格式
    postingdate: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)  # 讓 Pydantic 能處理 ORM
