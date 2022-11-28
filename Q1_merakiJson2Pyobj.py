'''Q.1 Json data ko python object main convert karne ka program likho?.'''
import json

with open("meraki_1.json") as f:
    data=json.load(f)

print(data)



