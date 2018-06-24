from mongoengine import *

#1. Design dâtbase
class Service(Document):
  name = StringField()
  dob = IntField()
  gender = IntField()
  height = IntField()
  phone = StringField()
  address = StringField()
  status = BooleanField()

# new_service = Service(
#   name="Hera",
#   dob=1995,
#   gender=0,
#   height=160,
#   phone="0123456789",
#   address="Hà Nội",
#   status=True
# )

# new_service = Service(
#   name="Fangqin",
#   dob=2000,
#   gender=0,
#   height=160,
#   phone="0123456789",
#   address="Hà Nội",
#   status=False
# )



# new_service.save()