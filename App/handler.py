from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from read import analizar_documento
from mocks import respuestas_mocks
import os


app = Flask(__name__)
api = Api(app)

# Retorna el contenido del archivo
class Devocional(Resource):
    def get(self):
        resp = analizar_documento('template2.docx')
        return jsonify(resp)

# Retorna los datos de prueba (52 semanas)
class Mocks(Resource):
    def get(self):
        page = request.args.get('page', default = 1, type = int)
        per_page = request.args.get('per_page', default = 10, type = int)
        resp = respuestas_mocks(page, per_page)
        return jsonify(resp)

api.add_resource(Devocional, '/devocional')
api.add_resource(Mocks, '/mocks')

if __name__ == '__main__':
    app.run(debug=True)
