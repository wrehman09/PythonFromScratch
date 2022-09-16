#Dictionaries  and nested list &  dictionaries in Python




# putting integer values
Dict = {1: 'firstelement', 2: '2element', 3: '3element'}

print(Dict)


dict={"one":"dell","two":"lenovo"}
print(dict["one"])

dict["three"]="hp"

print(dict)

for key in dict:
    print(key)
    print(dict[key])

#nested list in dict
dict={
    "France":["Paris","Lillie","Dijon"],
    "India":["Noida","Delhi","Pune"],
    "Germany":["Berlin","Hamburg"]
}

print(dict["France"][1])
#nested dict in dict

dict={
    "France":{"cities_visited":["Paris","","Dijon"],"notvisited":["Lillie"]},
    "India":{"cities_visited":["Noida","","Pune"],"notvisited":["Delhi"]},
    "Germany":{"cities_visited":["","Hamburg"],"notvisited":["Berlin"]}
}

#nested dict in list 
print(dict["India"]["cities_visited"][0])
list=[
    
    {"France":["Paris","Lillie","Dijon"],
    "India":["Noida","Delhi","Pune"],},
    {
        "Germany":["Berlin","Hamburg"]
} 
]

print(list[0]["France"][0])

