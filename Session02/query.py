from models.service import Service
import mlab

mlab.connect()

# all_service = Service.objects()
# first_service = all_service[0]

# # print(first_service['name'])
# print(first_service.address)
# #to_mongo : lấy dữ liệu

id_to_find = "5b2baf85c1318f2d4ca93114"

# hera = Service.objects().get(id=id_to_find)


# print(hera.to_mongo())   #list ra hết các phần tử
service = Service.objects().with_id(id_to_find)

# hera = Service.objects(id=id_to_find)
# print(rm)

# print(rm.to_mongo())

# hera.delete() #xóa


#--------------------
if service is not None:

    # hera.delete()
    #print("Deleted")
    print(service.dob)
    service.update(set__dob=1995) #update thông tin
    service.reload()   #cập nhất thông tin 
    
    print(service.dob)
else:
    print("Service not found")

#---------------------- Kiểm tra