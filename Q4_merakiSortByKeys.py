import json


d={'4': 5, '6': 7, '1': 3, '2': 4}
p=sorted(d)
# print(p)
d1={}
for i in p:
    if i in d:
        d1[i]=d[i]
# print(d1)

with open("sorted.json",'w') as file:
    json.dump(d1,file)