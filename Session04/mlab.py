import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds119160.mlab.com:19160/c4e18-csm-app

host = "ds119160.mlab.com"
port = 19160
db_name = "c4e18-csm-app"
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