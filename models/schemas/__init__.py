from .card_info_schema import CardInfoSchema
from .card_info_update_schema import CardInfoUpdateSchema
from .card_info_create_schema import CardInfoCreateSchema
# from .consumption_create_schema import ConsumptionCreateSchema
from .category_schema import CategorySchema
from .transaction_schema import TransactionSchema
from .transaction_update_schema import TransactionUpdateSchema
from .transaction_create_schema import TransactionCreateSchema
from .transaction_method_schema import TransactionMethodSchema

SCHEMA_CATEGORIES = {
    "cards": ["CardInfoSchema", "CardInfoUpdateSchema", "CardInfoCreateSchema"],
    "category": ["CategorySchema"]
}

__all__ = [
    *SCHEMA_CATEGORIES["cards"],
    *SCHEMA_CATEGORIES["category"]
]
