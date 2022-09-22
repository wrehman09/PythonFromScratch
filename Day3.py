#Day 3 ..Module Concept 
# File can be imported using import filename method , variable is also imported with the import 
# random module 
import random

#randomnumber
randomNumber=random.randint(1,10)
#generate number between 0,1 
randomfloating=random.random() 
print(randomNumber)
print(randomfloating)


#function in python is used by keyword def 

def hello(name):
    print("hello "+name)

hello("wasi")


#arguments 


def argument(*args):
    for n in args:
        print(n)


argument(3,4,5,6,7)

def kargs(**kwargs):
    print(kwargs["c"])
    

kargs(a=2,b=3,c=4)