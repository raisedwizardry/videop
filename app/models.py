from . import db


class Listed(db.Model):
    __tablename__ = 'listeds'
    id = db.Column(db.Integer, primary_key=True)
    directory = db.Column(db.String(64))
    dirfilename = db.Column(db.String(64))
    filename = db.Column(db.String(64))
    filenamenoext = db.Column(db.String(64))
    epnum= db.Column(db.String(64))
    epseason= db.Column(db.String(64))
    epshow= db.Column(db.String(64))
    epname= db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<Name %r>' % self.epname 