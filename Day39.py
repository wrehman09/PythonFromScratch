#insertion sort
inparray=[6,5,3,1,8,7,2,4]

for i in range(len(inparray)):
    a=i
    for j in range(i-1,-1,-1):
        #print(f"compare {inparray[i]} and {inparray[j]} ")
        if(inparray[a]<inparray[j]):
            temp=inparray[a]
            inparray[a]=inparray[j]
            inparray[j]=temp
            a=a-1
        else:
            break
        #print(f"inside {inparray}")
    print(f"{inparray}")




