from enum import unique
from werkzeug.security import generate_password_hash, check_password_hash
from project import db, ma

class User(db.Model):
    # this is called danda abstract
    # __abstract__ = True # This means that we are not going to create a table from this class
    __tablename__ = 'users' # When we wanna create a table from this class we specify the name of the table like this

    # Defining our fields
    uid = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    middlename = db.Column(db.String(50))
    lastname = db.Column(db.String(50), nullable=False)
    phonenumber = db.Column(db.String(15))
    email = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(256))

    # Defining the class constructor
    def __init__(self, firstname, middlename, lastname, phonenumber, email, username, password) -> None:
        self.firstname = firstname.title()
        self.middlename = middlename.title()
        self.lastname = lastname.title()
        self.phonenumber = phonenumber
        self.email = email.lower()
        self.username = username.lower()
        self.set_password(password)

    # Here we will create our class function to hash the password
    def set_password(self, password):
        self.password = generate_password_hash(password)

    # This class method is to compare between the hashed password we have in our database
    # and the text password given by the user
    def check_password(self, password):
        return check_password_hash(self.password, password)

# users schema
# Now we are going to use marshmallow to serialize our schema
class UserSchema(ma.Schema):
    class Meta:
        fields = ('uid', 'firstname', 'middlename', 'lastname', 'phonenumber', 'email')

# initialize the user schema
user_schema = UserSchema()
users_schema = UserSchema(many=True)

# We will create a test class for our users class
