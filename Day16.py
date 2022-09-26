#write into json  - bunch of key value nested dictionary can be used to serialise and desierlise json 

import json


data={
    "Amazon":{
        "email":"testemail",
        "password":"testpassword"
    }
}

#dump data into json
with open("data.json","w") as data_file:
    json.dump(data,data_file,indent=4)


#load data from json
with open("data.json") as data_file:
    data=json.load(data_file)
    print(data)
    print(data["Amazon"]["email"])



new_data={
    "Twitter":{
        "email":"testemail",
        "password":"testpassword"
    }
}

#dump data into json reading , updating old and save new data to file 
with open("data.json",) as data_file:
    data=json.load(data_file)
    data.update(new_data)
with open("data.json","w") as data_file:
    json.dump(data,data_file,indent=4)
