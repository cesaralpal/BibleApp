from flask import Flask, jsonify
from flask_restful import Resource, Api
from read import analizar_documento
import os


app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        resp = analizar_documento('template2.docx')
        return jsonify(resp)

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
