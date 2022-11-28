d={}
with open("convertInJson.txt","r") as f:
  for i in f:
    s=i.split()
    d[s[0]]=s[1]
# print(d)

import json

with open("convert2json.json","w") as f:
    json.dump(d,f, indent=2)