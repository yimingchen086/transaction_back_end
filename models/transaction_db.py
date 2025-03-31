from exts import db
from datetime import datetime


class Transaction(db.Model):
    __tablename__ = 'transaction'

    transaction_id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 交易ID，主鍵
    transaction_method_id = db.Column(db.Integer, db.ForeignKey('transaction_method.method_id'),
                                      nullable=False)  # 交易方法ID，外鍵
    transaction_title = db.Column(db.String(50), nullable=False)  # 交易標題
    amount = db.Column(db.Numeric(10, 2), nullable=False)  # 交易金額
    category_id = db.Column(db.Integer, db.ForeignKey('category.category_id'), nullable=False)  # 類別ID，外鍵
    transaction_time = db.Column(db.DateTime(timezone=True))  # 交易時間
    create_time = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)  # 創建時間，默認為當前時間
    card_id = db.Column(db.Integer, db.ForeignKey('credit_card.card_id'), nullable=False)  # 卡片ID，外鍵
    store = db.Column(db.String(50), nullable=False)
    actual_amount = db.Column(db.Integer)

    # 定義外鍵關係
    transaction_method = db.relationship('TransactionMethod', backref='transactions')
    category = db.relationship('Category', backref='transactions')
    card = db.relationship('CardInfo', backref='transactions')
