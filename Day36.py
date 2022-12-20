def fact(n):
    if n!=1:
        return n*fact(n-1)
    else:
        return 1

print(fact(5))


def facti(n):
    fact=1
    for num in range(n,1,-1):
        fact=num*fact
    return fact

print(facti(4))


def fibi(n):
    a=0
    b=1
    for num in range(1,n):
       bo=b
       b=b+a
       a=bo
       

    return b

print(fibi(12))




def fib(n):
    if(n==1):
        return 1
    elif(n<=0):
        return 0
    else:
        return fib(n-1)+fib(n-2)

print(fib(12))



def rev_str(str):
    strarray=str.split()
    strtr=""
    if len(strarray)> 1:
        for i in strarray:
           strtr=rev_str(i)+" "+strtr
    else:
        strtr=str[::-1]
    return strtr.strip()

   


def reverse_str(str):
    strt=""
    if len(str)>=2:
        strt=reverse_str(str[0:-2])

    else:
        strt=str
    return strt






print(reverse_str("yoyo mastery"))