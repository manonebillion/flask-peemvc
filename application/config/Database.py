from peewee import Model,SqliteDatabase

db = SqliteDatabase('carsweb.db')

class BaseModel(Model):
    class Meta:
        database = db
