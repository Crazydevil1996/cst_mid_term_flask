from database.db import db


class books(db.Document):
    b_id = db.IntField(required=True, unique=True)
    author = db.StringField(required=True)
    country = db.StringField(required=True)
    imageLink = db.StringField(required=True)
    language = db.StringField(required=True)
    link = db.StringField(required=True)
    pages = db.IntField(required=True)
    title = db.StringField(required=True)
    year = db.IntField(required=True)