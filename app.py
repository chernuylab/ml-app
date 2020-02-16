from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Predict(Resource):

    def post(self, data):
        pass

api.add_resource(Predict, '/')

app.run(port=5000, debug=true)
