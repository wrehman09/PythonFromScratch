#selection sort

inparray=[6,5,3,1,8,7,2,4]
lens = len(inparray)
for m in range(lens):
    test = 'yes'
    mval = inparray[m]
    shortest = inparray[m]
    for n in range(m,lens-1):
        if shortest > inparray[n+1]:
            print(shortest,inparray[n+1])
            # print(inparray[n],inparray[n+1])
            shortest = inparray[n+1]
            vals = n+1
            test = 'no'
    if test == 'no':    
        inparray[m] = shortest
        inparray[vals] = mval
        shortest = inparray[m]
        print(inparray)

print(inparray)

#second way
    
inparray=[8,5,2,6,9,3,1,4,0,7]
print(inparray)

smallest, j=100000,-1
length=len(inparray)
for i in range(length):
    for pos in range(i,length):
        if(inparray[pos]<smallest):
            smallest=inparray[pos]
            j=pos
            

    temp=inparray[i]
    inparray[i]=inparray[j]
    inparray[j]=temp
    
    smallest=100000
    print(inparray)
