#Day 5 while loop and hangman game 
import random


i=0
while(i<6):
    print(i)
    i=i+1
print("loop break")






words = "afforest,aftermath,blithesome,broadsheet,buffoonish,caprice,capricious,causerie,chivalrous,congratulatory,dapper,debonaire,devil-may-care,emblazon,eudaemonia,extremum,exultant,featherbrained,felicity"

word_list=words.split(",")
random_word=random.choice(word_list)
#print(random_word)
life=4 
wordfound=len(random_word)
random_word2=["_"]*len(random_word)
print(random_word2)
i=0
while ( life>0 and wordfound>0 ):
    inpcharacter=input("Guess any character " +str(life)+ "life")
    charfound=False
    for charac in random_word:
        if(charac==inpcharacter):
            random_word2[i]=inpcharacter
            charfound=True
            wordfound=wordfound-1
        
        i=i+1
    if(charfound==False):
        life=life-1    
    print(random_word2)
    i=0

if(wordfound==0):
    print("You Won")
else:
    print("Game over")
    print(random_word)

    

 