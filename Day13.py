#gui using tkinter   button label like  windows form 


import tkinter #documentAation is to refer 

def buttonClick():
    print("Button clicked")


window= tkinter.Tk()
window.title("GUI Program")
window.minsize(width=500,height=600)

#label 
my_label=tkinter.Label(text="Welcome to Python GUI using Tkinter") 
# my_label["text"]="welcome "  #text can be set by this way also 
my_label.pack() 


def buttonClick():
    print("Button clicked")
    my_label.config(text=input.get())


mybutton=tkinter.Button(text="Submit",command=buttonClick)


mybutton.pack(side="right")

name_label=tkinter.Label(text="Name")
name_label.pack(side="left",) 

input= tkinter.Entry()
input.pack(side="left")

#layout manager pack , place , grid 

placelabel=tkinter.Label(text="place label")
placelabel.place(x=40,y=70)


# to be used when only grid is usewd not with other layout  inside Day13_2
#gridlabel=tkinter.Label(text="grid label")
#gridlabel.grid(column=0 ,row=0)

window.mainloop()
