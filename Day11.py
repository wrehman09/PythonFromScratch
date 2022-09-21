#list comprehension && dictionary comprehension

list=[1,2,3]
new_list=[item+1 for item in list ]
print(new_list)

name="wasi"
newnamelist=[letter for letter in name]
print(newnamelist)

#sequence--> list range string tuple 

rangelist=[num *2 for num in range(1,5)]
print(rangelist)

#conditional list comprehension 

name=["alex","beth","caroline","dave","elanor","freddie"]


new_namelist=[newitem.upper() for newitem in name if len(newitem)>5 ]
print(new_namelist)


newdict={item:item+"test" for item in name}

print(newdict)

dict={
"one":1,
"two":2
}

newdict={key:value+1 for (key,value) in dict.items()}

print(newdict)