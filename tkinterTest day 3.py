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
