d={
    "shopping_list":
        { 
            "chaco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        } 
}

import json

with open("shopping.json",'w') as f:
    json.dump(d,f,indent=2)

item=input('enter item:-')
qty=int(input('enter qty:-'))

with open('shopping.json') as file:
    data=json.load(file)

if item in data["shopping_list"]:
    data["shopping_list"][item]=int(data["shopping_list"][item])-qty

with open("shopping.json",'w') as nfile:
    json.dump(data,nfile,indent=2)