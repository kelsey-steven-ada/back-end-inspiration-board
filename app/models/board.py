from app import db

class Board(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    owner = db.Column(db.String, nullable=False)
    cards = db.relationship("Card", back_populates="board")

    def to_dict(self):
        cards_info = [card.to_dict() for card in self.cards]
        return {
            "id": self.id,
            "name": self.name,
            "owner": self.owner,
            "cards": cards_info
    }

    @classmethod
    def from_dict(cls, data_dict):
        return cls(
            name=data_dict["name"],
            owner=data_dict["owner"]
        )