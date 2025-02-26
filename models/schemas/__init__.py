from .card_info_schema import CardInfoSchema
from .card_info_update_schema import CardInfoUpdateSchema
from .card_info_create_schema import CardInfoCreateSchema
# from .consumption_create_schema import ConsumptionCreateSchema
from .category_schema import CategorySchema


SCHEMA_CATEGORIES = {
    "cards": ["CardInfoSchema", "CardInfoUpdateSchema", "CardInfoCreateSchema"],
    # "consumption": ["ConsumptionCreateSchema"]
    "category": ["CategorySchema"]
}

__all__ = [
    *SCHEMA_CATEGORIES["cards"],
    # *SCHEMA_CATEGORIES["consumption"]
    *SCHEMA_CATEGORIES["category"]
]
