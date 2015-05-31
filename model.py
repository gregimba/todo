from peewee import *
import datetime

db = SqliteDatabase('app.db')

class BaseModel(Model):
    class Meta:
        database = db

class Item(BaseModel):
    name = CharField()
    description = TextField()
    done = BooleanField(default=False)

def create_tables():
    db.connect()
    db.create_tables([Item])