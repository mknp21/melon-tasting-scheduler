"""Drop db, create db, and automatically populate db with data."""

import crud
import model
# import server

from faker import Faker
fake = Faker()

os.system('dropdb rezzies')
os.system('createdb rezzies')

model.connect_to_db(server.app)
model.db.create_all()

