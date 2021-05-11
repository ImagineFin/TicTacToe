# -= Made in python 3.9 5/5/2021 - 5/6/2021 (2 days). Made by Fin#2354 =-
# Variables and imports.
from tkinter import *
root = Tk()
root.title('TicTacToe')
root.resizable(width=False, height=False)
WhosTurn = 'X'
oImage = PhotoImage(file='O.png')
xImage = PhotoImage(file='X.png')
StartingImage = PhotoImage(file='Start.png')

XOImage1 = StartingImage
XOImage2 = StartingImage
XOImage3 = StartingImage
XOImage4 = StartingImage
XOImage5 = StartingImage
XOImage6 = StartingImage
XOImage7 = StartingImage
XOImage8 = StartingImage
XOImage9 = StartingImage

# This defines whos going next.
def NextTurn():
    global WhosTurn 
    if WhosTurn == 'X':
        WhosTurn = 'O'    
    else:
        if WhosTurn == 'O':
            WhosTurn = 'X'
    print(WhosTurn)

# This changes the image when the square is clicked depending on whos turn it is.
def ChangeImage1():
    global xImage
    global oImage
    global XOImage1
    if WhosTurn == 'X':
        XOImage1 = oImage
        button1['image'] = XOImage1
    else:
        if WhosTurn == 'O':
            XOImage1 = xImage
            button1['image'] = XOImage1
def ChangeImage2():
    global xImage
    global oImage
    global XOImage2
    if WhosTurn == 'X':
        XOImage2 = oImage
        button2['image'] = XOImage2
    else:
        if WhosTurn == 'O':
            XOImage2 = xImage
            button2['image'] = XOImage2
def ChangeImage3():
    global xImage
    global oImage
    global XOImage3
    if WhosTurn == 'X':
        XOImage3 = oImage
        button3['image'] = XOImage3
    else:
        if WhosTurn == 'O':
            XOImage3 = xImage
            button3['image'] = XOImage3
def ChangeImage4():
    global xImage
    global oImage
    global XOImage4
    if WhosTurn == 'X':
        XOImage4 = oImage
        button4['image'] = XOImage4
    else:
        if WhosTurn == 'O':
            XOImage4 = xImage
            button4['image'] = XOImage4
def ChangeImage5():
    global xImage
    global oImage
    global XOImage5
    if WhosTurn == 'X':
        XOImage5 = oImage
        button5['image'] = XOImage5
    else:
        if WhosTurn == 'O':
            XOImage5 = xImage
            button5['image'] = XOImage5
def ChangeImage6():
    global xImage
    global oImage
    global XOImage6
    if WhosTurn == 'X':
        XOImage6 = oImage
        button6['image'] = XOImage6
    else:
        if WhosTurn == 'O':
            XOImage6 = xImage
            button6['image'] = XOImage6
def ChangeImage7():
    global xImage
    global oImage
    global XOImage7
    if WhosTurn == 'X':
        XOImage7 = oImage
        button7['image'] = XOImage7
    else:
        if WhosTurn == 'O':
            XOImage7 = xImage
            button7['image'] = XOImage7
def ChangeImage8():
    global xImage
    global oImage
    global XOImage8
    if WhosTurn == 'X':
        XOImage8 = oImage
        button8['image'] = XOImage8
    else:
        if WhosTurn == 'O':
            XOImage8 = xImage
            button8['image'] = XOImage8
def ChangeImage9():
    global xImage
    global oImage
    global XOImage9
    if WhosTurn == 'X':
        XOImage9 = oImage
        button9['image'] = XOImage9
    else:
        if WhosTurn == 'O':
            XOImage9 = xImage
            button9['image'] = XOImage9

# Disables the button when its clicked
def Disable1():
    button1['state'] = DISABLED
def Disable2():
    button2['state'] = DISABLED
def Disable3():
    button3['state'] = DISABLED
def Disable4():
    button4['state'] = DISABLED
def Disable5():
    button5['state'] = DISABLED
def Disable6():
    button6['state'] = DISABLED
def Disable7():
    button7['state'] = DISABLED
def Disable8():
    button8['state'] = DISABLED
def Disable9():
    button9['state'] = DISABLED

# This changes the label at the bottom and displays whos turn it is.
def ChangeWhosTurnLabel(): 
    WhosTurnLabel['text'] = "It's " + WhosTurn + "'s turn."

# Background color and placeholder for the size
background = Canvas(width='500', height='500', bg='#9EADC8')
background.pack()

# Label for whos turn it is
WhosTurnLabel = Label(text= "It's " + WhosTurn + "'s turn.")
WhosTurnLabel.pack()
#BoardImage
boardimage = PhotoImage(file='TikTacToe.png')
background.create_image(250, 250, image=boardimage,)

#Buttons that display X/O depending on whos turn
button1 = Button(command=lambda: [Disable1(), NextTurn(), ChangeImage1(), ChangeWhosTurnLabel(), ChangeWhosTurnLabel()], image=XOImage1, width='90', height='90', bg='#9EADC8', activebackground='#9eadc8', borderwidth=0,)
button1.place(relx=0.19, rely=0.18)
button2 = Button(command=lambda: [Disable2(), NextTurn(), ChangeImage2(), ChangeWhosTurnLabel(), ChangeWhosTurnLabel()], image=XOImage2, width='90', height='90', bg='#9EADC8', activebackground='#9eadc8', borderwidth=0)
button2.place(relx=0.4, rely=0.18)
button3 = Button(command=lambda: [Disable3(), NextTurn(), ChangeImage3(), ChangeWhosTurnLabel(), ChangeWhosTurnLabel()], image=XOImage3, width='90', height='90', bg='#9EADC8', activebackground='#9eadc8', borderwidth=0)
button3.place(relx=0.61, rely=0.18)
button4 = Button(command=lambda: [Disable4(), NextTurn(), ChangeImage4(), ChangeWhosTurnLabel(), ChangeWhosTurnLabel()], image=XOImage4, width='90', height='90', bg='#9EADC8', activebackground='#9eadc8', borderwidth=0)
button4.place(relx=0.19, rely=0.38)
button5 = Button(command=lambda: [Disable5(), NextTurn(), ChangeImage5(), ChangeWhosTurnLabel(), ChangeWhosTurnLabel()], image=XOImage5, width='90', height='90', bg='#9EADC8', activebackground='#9eadc8', borderwidth=0)
button5.place(relx=0.4, rely=0.38)
button6 = Button(command=lambda: [Disable6(), NextTurn(), ChangeImage6(), ChangeWhosTurnLabel(), ChangeWhosTurnLabel()], image=XOImage6, width='90', height='90', bg='#9EADC8', activebackground='#9eadc8', borderwidth=0)
button6.place(relx=0.61, rely=0.38)
button7 = Button(command=lambda: [Disable7(), NextTurn(), ChangeImage7(), ChangeWhosTurnLabel(), ChangeWhosTurnLabel()], image=XOImage7, width='90', height='90', bg='#9EADC8', activebackground='#9eadc8', borderwidth=0)
button7.place(relx=0.19, rely=0.59)
button8 = Button(command=lambda: [Disable8(), NextTurn(), ChangeImage8(), ChangeWhosTurnLabel(), ChangeWhosTurnLabel()], image=XOImage8, width='90', height='90', bg='#9EADC8', activebackground='#9eadc8', borderwidth=0)
button8.place(relx=0.4, rely=0.59)
button9 = Button(command=lambda: [Disable9(), NextTurn(), ChangeImage9(), ChangeWhosTurnLabel(), ChangeWhosTurnLabel()], image=XOImage9, width='90', height='90', bg='#9EADC8', activebackground='#9eadc8', borderwidth=0)
button9.place(relx=0.618, rely=0.59)

print(WhosTurn)
root.mainloop()