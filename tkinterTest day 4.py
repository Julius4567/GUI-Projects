from tkinter import *

top = Tk()
songList = []

def addTrack():
    songList.append(E1.get())
    E1.delete(0, END)
                    

def printList():
    print (songList)

def exportList():
    with open("test.txt", "w") as f:
        for item in songList:
            f.write("%s\n" % item)
            
def clearWindow():
    for widget in top.winfo_children():
        widget.destroy()

def mainMenu():
    clearWindow()
    LMain = Label(top, text= "Block 5 GUI Projects")
    LMain.grid(column = 0, row= 1)
    
    B1Main = Button(top, text= "Week 1", bg = "gray", command = week1)
    B1Main.grid(column = 0, row= 2)
    
    B2Main = Button(top, text= "Week 2", bg = "gray")
    B2Main.grid(column = 0, row= 3)
    
    B3Main = Button(top, text= "Week 3", bg = "gray")
    B3Main.grid(column = 0, row= 4)

if __name__ == "__main__":
    mainMenu()
    top.mainloop()
    
def week1():
    clearWindow()
    #This is a Label widget
    L1 = Label(top, text="ourTunes")
    L1.grid(column= 0, row= 1)

    #This is an Entry widget (for text entry)
    E1 = Entry(top, bd = 5)
    E1.grid(column= 0, row = 2)

    #This is a Button widget
    B1 = Button(top, text= " + ",  bg = "white", command = addTrack)
    B1.grid(column= 1, row= 2)

    B2 = Button(top, text= "Playlist", bg = "#d4850f", command = printList)
    B2.grid(column= 1, row= 1)

    B3 = Button(text= "Export", bg= "#4940e6", command= exportList)
    B3.grid(column= 1, row = 3)



top.mainloop()
