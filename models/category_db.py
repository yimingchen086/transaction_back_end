from exts import db
from sqlalchemy.dialects.postgresql import ENUM

# 假設transaction_type是一個自定義的ENUM類型
transaction_type = ENUM('income', 'expense', name='transaction_type')


class Category(db.Model):
    __tablename__ = 'category'

    category_id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 類別ID，主鍵
    category_name = db.Column(db.String(100), nullable=False)  # 類別名稱
    transaction_type = db.Column(transaction_type, nullable=False)  # 交易類型