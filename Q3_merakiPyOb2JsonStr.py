import json


d={
    "name": "David", 
    "class": "I", 
    "age": 6
}

data=json.dumps(d)
print(data)
print(type(data))