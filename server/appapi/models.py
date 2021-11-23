"""
models.py
- Data classes for the application

Created by Xiong, Kaijie on 2021-11-24.
Copyright © 2021 Xiong, Kaijie & Xu, Shuoni. All rights reserved.
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Card(db.Model):
    __tablename__ = 'cards'

    id = db.Column(db.Integer, primary_key=True)
    cardType = db.Column(db.String(16), nullable=False)
    cardBgColor = db.Column(db.String(255), nullable=False)
    cardBgOpacity = db.Column(db.Float, nullable=False)
    cardHeight = db.Column(db.String(120), nullable=False)

    def __init__(self, cardType, cardBgColor, cardBgOpacity, cardHeight):
        self.cardType = cardType
        self.cardBgColor = cardBgColor
        self.cardBgOpacity = cardBgOpacity
        self.cardHeight = cardHeight

    def to_dict(self):
        cardStyleDict = dict(cardBgColor = self.cardBgColor,
                         cardBgOpacity = self.cardBgOpacity,
                         cardHeight = self.cardHeight
                        )
        return dict(id = self.id,
                    cardType = self.cardType,
                    cardStyle = cardStyleDict
                    )
