from app import db

class Lead(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<Lead %r>' % self.id