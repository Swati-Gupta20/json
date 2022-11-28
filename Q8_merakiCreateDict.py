l=[['neelam','programer','24','2400'],
['komal','trainer','24','20000'],
['anuradha','HR','25','40000'],
['Abhishek','manager','29','63000']]

k=['name','designation','age','salary']
sk=['emp1','emp2','emp3','emp4']
d={}

for i in range(len(l)):
    d1={}
    for j in range(len(l)):
        d1[k[j]]=l[i][j]
    d[sk[i]]=d1
print(d)

import json
with open("createDict.json",'w') as f:
    json.dump(d,f, indent=4)