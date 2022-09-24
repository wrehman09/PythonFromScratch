#Pomodoro application using tkinter  
import math


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20 
MARK="✔"

rep=1
work=1
def Start():
    print("Started")
    label.config(text="Work",fg=GREEN)
    countdown(WORK_MIN*60)

def counter(rep):
     #rep=1 ,3, 5,7, WORK_MIN
     #rep 2,4,6, SHORT_BREAK_MIN
     #rep 8  LONG_BREAK_MIN

    if rep==8:
        label.config(text="Long Break",fg=RED)
        countdown(LONG_BREAK_MIN*60)
    elif rep%2 ==0:
        label.config(text="Break",fg=PINK)
        countdown(SHORT_BREAK_MIN*60)
    else:
        label.config(text="Work",fg=GREEN)
        global work
        work =work+1
        countdown(WORK_MIN*60)





def Reset():
    print("Reset")

def countdown(count):
    global rep
    mintime=math.floor(count/60)
    sectime=count%60
    if sectime <10:
        sectime=f"0{sectime}"


    
    canvas.itemconfig(timertext,text=f"{mintime}:{sectime}")
    if count>0:
        window.after(1000,countdown,count-1)
    else:
        global work
        ticktext=""
        for t in range(0,work):
            ticktext=ticktext+MARK

    
        ticklabel.config(text=ticktext)
        rep=rep+1
        counter(rep)


from cgitb import reset, text
import tkinter 

window= tkinter.Tk()

window.title("Pomodoro App")
window.config(padx=100,pady=50,bg=YELLOW)



label=tkinter.Label(text="Timer")
label.config(fg=GREEN,bg=YELLOW,font=["COURIER",35,"bold"])
label.grid(row=0,column=2)

canvas=tkinter.Canvas(height=224,width=200,bg=YELLOW,highlightthickness=0)
tomato_img=tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timertext=canvas.create_text(100,130,text="00:00", fill="white",font=["COURIER",35,"bold"])
##canvas.create_text(100,0,text="Timer", fill="green",font=["COURIER",35,"bold"])
canvas.grid(row=1,column=2)

startbutton=tkinter.Button(text="Start",command=Start)
startbutton.grid(row=2,column=0)
resetbutton=tkinter.Button(text="Reset",command=Reset)
resetbutton.grid(row=2,column=3)

ticklabel=tkinter.Label()
ticklabel.grid(row=3,column=2)

window.mainloop()



