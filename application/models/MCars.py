from application.config.Database import BaseModel
from peewee import TextField

class TBCarsWeb(BaseModel):
    carid = TextField()
    carname = TextField()
    carbrand = TextField() 
    carmodel = TextField()
    carprice = TextField()
    

    