# We will use our User model to populate our db with fake data
from .models import User
from project import db
from faker import Faker
# This is a global variable
fake = Faker()

def fake_data(record_number):
    for i in range(0, record_number):
        full_name = fake.name() # Mohamed BenAmmar
        firstname, lastname = full_name.split(' ', 1)
        email = fake.email()

        fake_user = User(firstname=firstname, middlename='', lastname= lastname,
        phonenumber='', username=full_name, email=email, password="project_pwd")
        db.session.add(fake_user)
        db.session.commit()
