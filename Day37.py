#buble sort 

inparray=[6,5,3,1,8,7,2,4]
# inparray=[1,2,3,4,5,6,7]
print(inparray)
# trick ='yes'
for m in inparray:
    trick = 'no'
    for n in range(len(inparray) - 1):
        if n+1 < len(inparray) :
            if inparray[n] > inparray[n+1]:
                trick = 'yes'
                temp = inparray[n]
                inparray[n]= inparray[n+1]
                inparray[n+1] = temp
        # print(inparray)
    if trick == 'no':
        break
        
    print(inparray)

print(inparray)


#2nd way
print("--------------------------------------------------------------------------------------")
inparray=[6,5,3,1,8,7,2,4]
#inparray=[1,2,3,4,5,6]
print(inparray)
noofpass=0
noofloop=0
for element in inparray:
    i,j=0,1
    for elem in inparray:
        if(j>len(inparray)-1):
            break
        if(inparray[i]>inparray[j]):
            inparray[i]=inparray[j]
            inparray[j]=elem
            noofpass+=1

        i+=1
        j+=1
        noofloop+=1
    
    if(noofpass==0):
        break
    print(inparray)
print(noofloop)


print(inparray)
    





