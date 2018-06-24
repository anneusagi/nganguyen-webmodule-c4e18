from models.service import Service
import mlab
from faker import Faker
from random import randint, choice


mlab.connect()

fake = Faker()

fake.name()
# print(fake.name())

for i in range(50):
    print("Saving Service", i + 1, ".....")
    new_service = Service(
        name=fake.name(),
        dob=randint(1990, 2000),
        gender=randint(0, 1),
        height=randint(155, 190),
        phone=fake.phone_number(),
        address=fake.address(),
        status=choice([True, False])
    )

    new_service.save()