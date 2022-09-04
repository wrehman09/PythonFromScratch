import re

#get number from string and sort them 
ip="1Node is r9ing in python3 4 last hours with gr8 speed"
trt=[int(no) for no in ip if no.isdigit()]
print (trt)
print(sorted(trt))

#check ip is valid
ip="1.10.5.1"
regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
if(re.search(regex, ip)):
        print("Valid Ip address")
 
else:
        print("Invalid Ip address")



#reverse of  string except special character
ipstring="ym eman si *5&^* zan"

trt=[]
for no in ipstring.split():
    if(no.isalpha()):
        rev=no[::-1]
    else:
        rev=no
    trt.append(rev)

print(' '.join(trt))


