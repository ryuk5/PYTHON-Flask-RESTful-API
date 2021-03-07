from flask import jsonify, request
from project.admin import blueprint
from flask_restful import Api, Resource

api = Api(blueprint)

# This is how we define a blueprint route
@blueprint.route('/', methods=['GET'])
def index():
    ReturnResponse = {
        'msg': 'Hi, we are in the admin index route !'
    }
    return jsonify(ReturnResponse), 200

# We can use the class based routing 
class Admin(Resource):
    def get(self, id=None):
        return('Hi, there is an admin other route')

    def post(self):
        pass

api.add_resource(Admin, '/anotherroute')