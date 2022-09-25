# Exceptional handling
# keyword try , except , else, finally 

try:
    file=open("abc.txt")
except: 
    print("there is ann error")
    file=open("abc.txt","w")
else: # else execute when no error 
    print("no error")
finally:
    print("finally block")



#ERROR SPECIFIC
try:
    file=open("abc.txt")
except FileNotFoundError: 
    print("there is ann error")
    file=open("abc.txt","w")



# raising own exception

raise KeyError("There is error made by us")