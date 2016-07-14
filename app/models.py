from datetime import datetime

from app import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    body = db.Column(db.Text)
    date = db.Column(db.Date)

    def __init__(self, title, body):
        # type: (object, object) -> object
        self.title = title
        self.body = body
        self.date = datetime.now().date()

    def __eq__(self, other):
        return self.title == other.title and self.body == other.body

    def __hash__(self):
        return self.title.__hash__ + self.body.__hash__

