from email.policy import default
from app import db

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    message = db.Column(db.String, nullable=False)
    likes = db.Column(db.Integer, nullable=False, default=0)
    board_id = db.Column(db.Integer, db.ForeignKey('board.id'))
    board = db.relationship("Board", back_populates="cards")

    def to_dict(self):
        return {
            "id": self.id,
            "message": self.message,
            "board_id": self.board_id,
            "likes": self.likes
    }

    @classmethod
    def from_dict(cls, data_dict):
        return cls(
            board=data_dict["board"],
            message=data_dict["message"]
        )