from models.service import Service
import mlab

mlab.connect()

id_to_find = "5b2ba89bc1318f37f03b5107"

id_find = Service.objects.get(id=id_to_find)
print(id_find.name)

