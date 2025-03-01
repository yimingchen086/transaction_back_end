from exts import db


class TransactionMethod(db.Model):
    __tablename__ = 'transaction_method'

    method_id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 方法ID，主鍵
    method_name = db.Column(db.String(100), nullable=False)  # 方法名稱