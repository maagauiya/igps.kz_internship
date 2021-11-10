import requests
from requests.api import head
from requests.models import HTTPBasicAuth
from pymongo import MongoClient

client=MongoClient("mongodb+srv://maagauiya:magauiyainc@cluster0.f7uie.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",connect=False)
db = client["zvontest"]
collection = db["test"]

cursor=collection.find({})
phone=''
for doc in cursor:
    if doc['state']==False:
        phone=doc['phone']



url = "https://lk.zvonobot.kz/apiCalls/create"

headers =  {
    'Content-Type': 'application/json'
}

params = {
    'sessionKey': '9ebbd0b25760557393a43064a92bae539d962103', 
    'format': 'xml', 
    'platformId': 1
}


data = {
    "apiKey": "bgc4GXe07YEWA5HJCXqmJLDYWnLGBvRrhMwtPxBSvTHVPYtDkfP5g9MzP2Wk",
    "phone": phone,
    "dutyPhone": 1,
    "record": {
        "id": "1061807",
        "gender": 1
    }
}
connect = requests.post(url, headers=headers, params=params,json = data)
print(connect)