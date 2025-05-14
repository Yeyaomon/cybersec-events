from . import db

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    items = db.relationship('Item', backref='category', lazy=True)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    value = db.Column(db.Float)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
