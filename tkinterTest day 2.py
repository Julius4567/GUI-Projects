from tkinter import *

top = Tk()
songList = []

def addTrack():
    songList.append(E1.get()

def printList():
    print (songList)

#This is a Label widget
L1 = Label(top, text="Playlist Generator")
L1.grid(column= 0, row= 1)

#This is an Entry widget (for text entry)
E1 = Entry(top, bd = 5)
E1.grid(column= 0, row = 2)

#This is a Button widget
B1 = Button(top, text="Add to Playlist",  bg = "white", command = addTrack)
B1.grid(column= 1, row= 2)

B2 = Button(top, text="Print Playlist", bg = "light blue", command = printList)
B2.grid(column= 1, row= 1)




top.mainloop()
