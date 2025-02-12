from .card_info_schema import CardInfoSchema
from .card_info_update_schema import CardInfoUpdateSchema
from .card_info_create_schema import CardInfoCreateSchema

SCHEMA_CATEGORIES = {
    "cards": ["CardInfoSchema", "CardInfoUpdateSchema", "CardInfoCreateSchema"],
}

__all__ = [
    *SCHEMA_CATEGORIES["cards"]
]
