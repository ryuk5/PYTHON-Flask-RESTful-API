from flask import jsonify, request
from project.base import blueprint
from flask_restful import Api, Resource

api = Api(blueprint)

@blueprint.route('/', methods=['GET'])
def index():
    ReturnResponse = {
        'msg': 'Hi, we are in the base route !'
    }
    return jsonify(ReturnResponse), 200

# We can use the class based routing 
class Base(Resource):
    def get(self, id=None):
        return('Hi, there is an other base route'), 200

    def post(self):
        pass

api.add_resource(Base, '/anotherroute')