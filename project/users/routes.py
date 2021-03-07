from flask import jsonify, request
from project.users import blueprint
from flask_restful import Api, Resource

# Importing the user model and the marshmallow user_schema
from .models import User, user_schema, users_schema
# Importing the db 
from project import db

api = Api(blueprint)

# This is the blueprint based routing
@blueprint.route('/gender', methods=['GET'])
def gender():
    Gender = {
        'Male': 1,
        'Female': 2,
        'Transgender': 3
    }

    # We will see how to invert key value in a python dict
    ReturnResponse = {v:k for k,v in Gender.items()} # the items method is predefined method in python
    return jsonify(ReturnResponse), 200

# Implementing a route for filtering users by first name 
@blueprint.route('/names/<fname>', methods=['GET'])
def names(fname):
    users = db.session.query(User).filter(User.firstname.like(fname+'%'))
    # In SQL this is eq to
    #  SELECT * FROM TABLENAME WHERE VARNAME LIKE A%
    return users_schema.jsonify(users), 200

# We can use the class based routing 
class Users(Resource):
    def get(self, uid=None):
        if uid is None:
            # Fetch all the records
            users = User.query.all()
            return users_schema.dump(users), 200
        else:
            # Fetch a single record based on the user uid passed in the URL
            user = User.query.get(uid)
            return user_schema.dump(user), 200

    def post(self):
        firstname = request.json['firstname']
        middlename = request.json['middlename']
        lastname = request.json['lastname']
        phonenumber = request.json['phonenumber']
        email = request.json['email']
        username = request.json['username']
        password = request.json['password']
        
        new_user = User(firstname, middlename, lastname, phonenumber, email, username, password)

        db.session.add(new_user)
        try:
            db.session.commit()
            # After registration I wanna see the object that had been registred in the db
            return user_schema.dump(new_user), 201 # this status stands for inserted succesfully
        except:
            db.session.rollback()
            return jsonify({"msg": "error, user already exists!"})
        finally:
            # Close the connection
            db.session.close()

    def put(self, uid):
        # Grab the user from the db
        user = User.query.get(uid)
        # Getting data from the req body
        firstname = request.json['firstname']
        middlename = request.json['middlename']
        lastname = request.json['lastname']
        phonenumber = request.json['phonenumber']
        email = request.json['email']
        username = request.json['username']
        password = request.json['password']
        
        # Assining new values to the user object
        user.firstname = firstname
        user.middlename = middlename
        user.lastname = lastname
        user.phonenumber = phonenumber
        user.email = email
        user.username = username
        user.password = password

        try:
            db.session.commit() # Commit the chnges to the db
            return user_schema.dump(user), 201
        except:
            ReturnResponse = {
                "msg": "Check if resource exists!"
            }
            return jsonify(ReturnResponse)
        finally:
            # Close the connection with the db
            db.session.close()
        
        
 # A7na fél blueprint bté3na 3ana url prefix = "/users" donc man7otouche houni URL juste 5alinéha '/'
 # makénéche bch iwali /users/users donc don't specify url houni 5ater déja él blueprint 3andou url prefix
api.add_resource(Users, '/', methods=['GET', 'POST'], endpoint='users')
api.add_resource(Users, '/<uid>', methods=['GET', 'PUT', 'DELETE'], endpoint='user')