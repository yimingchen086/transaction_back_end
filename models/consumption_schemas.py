from pydantic import BaseModel


class ConsumptionSchema(BaseModel):
    amount: int
    store: str
    item: list[str]
    card_id: int