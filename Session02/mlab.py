import mongoengine
# mongodb://<dbuser>:<dbpassword>@ds161620.mlab.com:61620/muadongkhonglanh-c4e18

host = "ds161620.mlab.com"
port = 61620
db_name = "muadongkhonglanh-c4e18"
user_name = "admin"
password = "admin123"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())