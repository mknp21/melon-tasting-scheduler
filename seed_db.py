"""Drop db, create db, and automatically populate db with data."""

import os

import crud
import model
import server

from faker import Faker
fake = Faker()

os.system('dropdb rezzies')
os.system('createdb rezzies')

model.connect_to_db(server.app)
model.db.create_all()

#creates fake users
for n in range(5):
    name = fake.name()
    email = f"user{n}@email.com"

    user = crud.create_user(name, email)