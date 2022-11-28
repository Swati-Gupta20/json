'''Q.2 Python object ko json data main convert karne ka program likho?'''
import json

d={
    "name": "David", 
    "class": "I", 
    "age": 6
}


with open ("orders.json","w")as file:
    a=json.dump(d,file)
