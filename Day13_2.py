#gui using tkinter   button label like  windows form 


import tkinter #documentAation is to refer 

def buttonClick():
    print("Button clicked")


window= tkinter.Tk()
window.title("GUI Program")
window.minsize(width=500,height=600)

# to be used when only grid is usewd not with other layout 
gridlabel=tkinter.Label(text="grid label")
gridlabel.grid(column=0 ,row=0)

window.mainloop()
