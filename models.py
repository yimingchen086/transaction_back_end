from exts import db
from datetime import datetime


class CardInfo(db.Model):
    __tablename__ = 'cards_info'
    card_id = db.Column(db.Integer, primary_key=True)  # 主鍵
    card_name = db.Column(db.String(50), nullable=False)  # 卡片名稱
    bank = db.Column(db.String(50), nullable=False)  # 發卡銀行
    maxconsume = db.Column(db.Integer, nullable=True)  # 最大消費額度
    curramount = db.Column(db.Integer, nullable=True)  # 目前消費金額
    description = db.Column(db.Text, nullable=True)  # 描述
    store = db.Column(db.Text, nullable=True)  # 適用商店
    rewardstype = db.Column(db.String(50), nullable=True)  # 獎勵類型
    daterange_start = db.Column(db.Date, nullable=True)  # 優惠開始日期
    daterange_end = db.Column(db.Date, nullable=True)  # 優惠結束日期
    postingdate = db.Column(db.String(10), nullable=True)  # 發布日期

    def to_dict(self):
        """將物件轉換為 JSON 格式"""
        return {
            "card_id": self.card_id,
            "card_name": self.card_name,
            "bank": self.bank,
            "maxconsume": self.maxconsume,
            "curramount": self.curramount,
            "description": self.description,
            "store": self.store,
            "rewardstype": self.rewardstype,
            "daterange_start": self.daterange_start.isoformat() if self.daterange_start else None,
            "daterange_end": self.daterange_end.isoformat() if self.daterange_end else None,
            "postingdate": self.postingdate,
        }