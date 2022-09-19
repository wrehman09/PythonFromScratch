#file system 

file=open("myfile.txt")  # open file 
content = file.read() # read content 

print(content)
file.close() # we have top close it to free the resources 



with open("myfile.txt") as file : # WITH keyword manages to close the file automatica;ly no need to close 
    content= file.read()
    print(content)

# to write we need to add mode as w

with open("myfile.txt",mode="w") as file : # WITH keyword manages to close the file automatica;ly no need to close 
    
    file.write("hi New Text")


# mail merge challenge  to merge 2 file text 


with open("letter.txt") as letterfile:
    lettercontent=letterfile.readlines()
   
    with open("name.txt") as namefile:
        names=namefile.readlines()
        for name in names:
            newconetent=str(lettercontent).replace("[name]",name)
            print(newconetent)