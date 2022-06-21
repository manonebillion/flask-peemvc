from application import api
from application.models.MCars import TBCarsWeb
from flask import jsonify
from flask_restx import reqparse,Resource

ns = api.namespace('cars', description='Cars API operations')
class Car(Resource):
    def get(self):
        rows = TBCarsWeb.select()    
        datas=[]

        for row in rows:
            datas.append({
            'carid':row.carid,
            'carname':row.carname,
            'carbrand':row.carbrand,
            'carmodel':row.carmodel,
            'carprice':row.carprice
        })
        return jsonify(datas)

ns.add_resource(Car, '/', endpoint="cars/")