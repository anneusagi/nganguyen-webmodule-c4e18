from models.service import Service

from faker import Faker
from random import randint, choice

# connect database
import mlab
mlab.connect()

fake = Faker()

# fake.name()
# print(fake.name())

new_service = Service(
    name="Tú Linh",
    dob=1994,
    gender=0,
    height=163,
    phone=fake.phone_number(),
    address=fake.address(),
    status=choice([True, False]),
    image="static/image/tulinh.jpg",
    description="Ngoan, xinh hiền",
    measurements=[90,60,90]
)

new_service.save()

