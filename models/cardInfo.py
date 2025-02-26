from exts import db


class CardInfo(db.Model):
    __tablename__ = 'credit_card'
    card_id = db.Column(db.Integer, primary_key=True)  # 卡片id 主鍵
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