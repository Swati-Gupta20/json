import json


x='{ "a":  1, "a":  2,"a":  3, "a": 4,"b": 1,"b": 2}'

data=json.loads(x)
print(data)