from tkinter import *
import tkinter
import random

top = Tk()
myList = []
songList = []
myRolls = []
rollTimes = 0
dieType = 0
Font_tuple = ("Forte", 20, "bold")
Mother = ("Elephant", 20, "bold")
Sans = ("Papyrus", 10, "bold")
colours = ['Red','Blue','Green','Pink','Black',
                    'Yellow','Orange','White','Purple','Brown']
score = 0
timeleft = 30

def printList():
    print(songList)

def exportList():
    with open("test.txt", "w") as f:
        for item in songList:
            f.write("%s\n" % item)
            
def clearWindow():
    for widget in top.winfo_children():
        widget.destroy()

def mainMenu():
    clearWindow()
    LMain = Label(top, text= "Block 5 GUI Projects", font = Font_tuple)
    LMain.grid(column = 0, row= 1)
    
    B1Main = Button(top, text= "Week 1", bg = "magenta", font = Mother, command = week1)
    B1Main.grid(column = 0, row= 2)
    
    B2Main = Button(top, text= "Week 2", bg = "magenta", font = Mother, command = week2)
    B2Main.grid(column = 0, row= 3)
    
    B3Main = Button(top, text= "Week 3", bg = "magenta", font = Mother, command = week3)
    B3Main.grid(column = 0, row= 4)
    
def week1():

    def addTrack():
        songList.append(E1.get())
        E1.delete(0, END)
    clearWindow()
                    

    clearWindow()
    #This is a Label widget
    L1 = Label(top, text="ourTunes", font = Mother)
    L1.grid(column= 0, row= 1)

    #This is an Entry widget (for text entry)
    E1 = Entry(top, bd = 5)
    E1.grid(column= 0, row = 2)

    #This is a Button widget
    B1 = Button(top, text= " + ",  bg = "white", font = Sans, command = addTrack)
    B1.grid(column= 1, row= 2)

    B2 = Button(top, text= "Playlist", bg = "#d4850f", font = Sans
                , command = printList)
    B2.grid(column= 1, row= 1)

    B3 = Button(text= "Export", bg= "cyan", font = Sans, command= exportList)
    B3.grid(column= 1, row = 3)

    B4 = Button(text="Main Menu", bg = "yellow", font = Sans, command= mainMenu)
    B4.grid(column= 0, row = 3)


def week2():
    def rollDice():
        
        #update varible date
        rollTimes = E2W2.get()
        dieType = E1W2.get()
        
        #clear window
        clearWindow()
        #calculate dice rolls
        for x in range(0, int(rollTimes)):
            myRolls.append(random.randint(1, int(dieType)))
            
        #display the rolls an exit button
        L4W2 = Label(top, text= "Here are your rolls!")
        L4W2.grid(column= 0, row= 1)
        
        L5W2 = Label(top, text= "{}".format(myRolls))
        L5W2.grid(column= 0, row= 2)
        
        B2W2 = Button(text="Main Menu", bg= "yellow", command = mainMenu)
        B2W2.grid(column= 0, row= 3)
        
        
    clearWindow()

    L1W2 = Label(top, text= "Dice Roller App")
    L1W2.grid(column= 2, row= 1)
    
    L2W2 = Label(top, text= "Number of Sides")
    L2W2.grid(column= 0, row= 2)
    
    L3W2 = Label(top, text="Number of Rolls")
    L3W2.grid(column= 3, row= 2)
    
    E1W2 = Entry(top, bd= 5)
    E1W2.grid(column= 0, row= 3)
              
    E2W2 = Entry(top, bd= 5)
    E2W2.grid(column= 3, row= 3)
              
    B1W2 = Button(text = "Roll 'em!", bg = "yellow", command = rollDice)
    B1W2.grid(column= 2, row= 4)

def week3():

    def startGame(event):
            
            if timeleft == 30:
                    countdown()
            nextColour()

    def nextColour():

            global score
            global timeleft
            if timeleft > 0:
                    e.focus_set()
                    if e.get().lower() == colours[1].lower():
                            
                            score += 1

                    e.delete(0, tkinter.END)
                    random.shuffle(colours)
                    label.config(fg = str(colours[1]), text = str(colours[0]))
                    scoreLabel.config(text = "Score: " + str(score))

    def countdown():
            global timeleft
            if timeleft > 0:
                    timeleft -= 1
                    timeLabel.config(text = "Time left: "
                                                            + str(timeleft))
                    timeLabel.after(1000, countdown)


    root = tkinter.Tk()
    root.title("COLORGAME")
    root.geometry("375x200")
    instructions = tkinter.Label(root, text = "Type in the colour"
                                                    "of the words, and not the word text!",
                                                                            font = ('Helvetica', 12))
    instructions.pack()


    scoreLabel = tkinter.Label(root, text = "Press enter to start",
                                                                        font = ('Helvetica', 12))
    scoreLabel.pack()
    timeLabel = tkinter.Label(root, text = "Time left: " +
                            str(timeleft), font = ('Helvetica', 12))                          
    timeLabel.pack()
    label = tkinter.Label(root, font = ('Helvetica', 60))
    label.pack()

    e = tkinter.Entry(root)
    root.bind('<Return>', startGame)
    e.pack()
    e.focus_set()
    root.mainloop()



 
if __name__ == "__main__":
    mainMenu()
    top.mainloop()

