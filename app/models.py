from . import db

class Userconfig(db.Model):
    __tablename__ = 'configs'
    id = db.Column(db.Integer, primary_key=True)
    plexdir = db.Column(db.String(64), unique=True)
    time = db.Column(db.Time())

    def __repr__(self):
        return '<Plex Directory %r>' % self.plexdir

class Listed(db.Model):
    __tablename__ = 'listeds'
    id = db.Column(db.Integer, primary_key=True)
    directory = db.Column(db.String(64))
    dirfilename = db.Column(db.String(64), unique=True)
    filename = db.Column(db.String(64) )
    filenamenoext = db.Column(db.String(64))
    epnum= db.Column(db.String(64))
    epseason= db.Column(db.String(64))
    epshow= db.Column(db.String(64))
    epname= db.Column(db.String(64))

    def __repr__(self):
        return '<Name %r>' % self.epname