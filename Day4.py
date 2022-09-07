#Day 4 we will learn list and a exercise .

#python data structure. it has 4 inbuilt data structure - list, dict, tuple and set 
# Python program to illustrate a list

# creates a empty list
nums = []

# appending data in list
nums.append(21)
nums.append(40.5)
nums.append("String")

print(nums)




#exercise to print x in treasure list at particular number
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

col=int(position[0])-1
row=int(position[1])-1
if(row==0):
    row1[col]="X"
elif(row==1):
    row2[col]="X"
elif(row==2):
    row3[col]="X"
else:
    print("Invalid row")

print(f"{row1}\n{row2}\n{row3}")
