from app import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    body = db.Column(db.Text)

    def __init__(self, title, body):
        # type: (object, object) -> object
        self.title = title
        self.body = body

    def __eq__(self, other):
        return self.title == other.title and self.body == other.body

    def __hash__(self):
        print "========"
        return self.title.__hash__ + self.body.__hash__

