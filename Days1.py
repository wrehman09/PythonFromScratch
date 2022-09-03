#Todays is the first day will be starting this 
#Print function will print and string number inside it 
print('Welcome to the Python 90 day of code its day 1')


#input will take any value from reader
#By default it takes string 
ipString=input("Enter string ")

#to get int we need to parse
ipnum=int(input("Enter the number"))


print(ipnum)
print(ipString)


#   Goal is to create a tip calculator which teach us type conversion and more understanding of datatype  


print("Welcome to Tip Calculator.")
bill=float(input("What was the total bill?"))
people=int(input("How many people to split the bill?"))
percentage=int(input("What percentage tip would you like to give ? 10, 12, or 15 ?"))
each=round(((bill+bill*percentage/100)/people),2)
print("each person should pay"+str(each))




#Conditions - In python we have if and else and elif  


if(ipnum%2==0):
    print("Num is even")
else:
    print("Num is odd")


#function in python is used by keyword def 

def hello(name):
    print("hello "+name)

hello("wasi")



#for loop 

for step in range(5):
    print(step)

fruits=["Apple","Peach"]

for fruit in fruits:
    print(fruit)





