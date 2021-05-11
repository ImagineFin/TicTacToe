# -= Made in python 3.9.5 at 5/5/2021 - 5/10/2021 (5 days). Made by Fin#2354 =-
# imports and Variables.
from tkinter import *
root = Tk()
root.title('TicTacToe')
root.resizable(width=False, height=False)
WhosTurn = 'X'
oImage = PhotoImage(file='O.png')
xImage = PhotoImage(file='X.png')
StartingImage = PhotoImage(file='Start.png')
IsDisabled = 'False'
WhatsInTL = '-'
WhatsInTM = '-'
WhatsInTR = '-'
WhatsInML = '-'
WhatsInMM = '-'
WhatsInMR = '-'
WhatsInBL = '-'
WhatsInBM = '-'
WhatsInBR = '-'
WinnerFound = 'False'

# This defines whos going next.
def NextTurn():
    global WhosTurn 
    if WhosTurn == 'X':
        WhosTurn = 'O'    
    else:
        if WhosTurn == 'O':
            WhosTurn = 'X'

# This changes the image when the square is clicked depending on whos turn it is. (TL referes to 'Top Left' ect.)
def ChangeImageTL():
    global xImage
    global oImage
    if WhosTurn == 'X':
        TL['image'] = oImage
    else:
        if WhosTurn == 'O':
            TL['image'] = xImage
def ChangeImageTM():
    global xImage
    global oImage
    if WhosTurn == 'X':
        TM['image'] = oImage
    else:
        if WhosTurn == 'O':
            TM['image'] = xImage
def ChangeImageTR():
    global xImage
    global oImage
    if WhosTurn == 'X':
        TR['image'] = oImage
    else:
        if WhosTurn == 'O':
            TR['image'] = xImage
def ChangeImageML():
    global xImage
    global oImage
    if WhosTurn == 'X':
        ML['image'] = oImage
    else:
        if WhosTurn == 'O':
            ML['image'] = xImage
def ChangeImageMM():
    global xImage
    global oImage
    if WhosTurn == 'X':
        MM['image'] = oImage
    else:
        if WhosTurn == 'O':
            MM['image'] = xImage
def ChangeImageMR():
    global xImage
    global oImage
    if WhosTurn == 'X':
        MR['image'] = oImage
    else:
        if WhosTurn == 'O':
            MR['image'] = xImage
def ChangeImageBL():
    global xImage
    global oImage
    if WhosTurn == 'X':
        BL['image'] = oImage
    else:
        if WhosTurn == 'O':
            BL['image'] = xImage
def ChangeImageBM():
    global xImage
    global oImage
    if WhosTurn == 'X':
        BM['image'] = oImage
    else:
        if WhosTurn == 'O':
            BM['image'] = xImage
def ChangeImageBR():
    global xImage
    global oImage
    if WhosTurn == 'X':
        BR['image'] = oImage
    else:
        if WhosTurn == 'O':
            BR['image'] = xImage

# Disables the button when its clicked
def DisableTL():
    TL['state'] = DISABLED
def DisableTM():
    TM['state'] = DISABLED
def DisableTR():
    TR['state'] = DISABLED
def DisableML():
    ML['state'] = DISABLED
def DisableMM():
    MM['state'] = DISABLED
def DisableMR():
    MR['state'] = DISABLED
def DisableBL():
    BL['state'] = DISABLED
def DisableBM():
    BM['state'] = DISABLED
def DisableBR():
    BR['state'] = DISABLED

# The next chunk of code keeps track of whats in each box, so in TL if theres a O/X I can refer to that later to see the theres 3 X's in a row.
def SeeWhatsInTL():
    global WhatsInTL
    WhatsInTL = '-'
    if TL['image'] == 'pyimage1':
        WhatsInTL = 'O'
    else:
        if TL['image'] == 'pyimage2':
            WhatsInTL = 'X'
def SeeWhatsInTM():
    global WhatsInTM
    if TM['image'] == 'pyimage1':
        WhatsInTM = 'O'
    else:
        if TM['image'] == 'pyimage2':
            WhatsInTM = 'X'
def SeeWhatsInTR():
    global WhatsInTR
    if TR['image'] == 'pyimage1':
        WhatsInTR = 'O'
    else:
        if TR['image'] == 'pyimage2':
            WhatsInTR = 'X'
def SeeWhatsInML():
    global WhatsInML
    if ML['image'] == 'pyimage1':
        WhatsInML = 'O'
    else:
        if ML['image'] == 'pyimage2':
            WhatsInML = 'X'
def SeeWhatsInMM():
    global WhatsInMM
    if MM['image'] == 'pyimage1':
        WhatsInMM = 'O'
    else:
        if MM['image'] == 'pyimage2':
            WhatsInMM = 'X'
def SeeWhatsInMR():
    global WhatsInMR
    if MR['image'] == 'pyimage1':
        WhatsInMR = 'O'
    else:
        if MR['image'] == 'pyimage2':
            WhatsInMR = 'X'
def SeeWhatsInBL():
    global WhatsInBL
    if BL['image'] == 'pyimage1':
        WhatsInBL = 'O'
    else:
        if BL['image'] == 'pyimage2':
            WhatsInBL = 'X'
def SeeWhatsInBM():
    global WhatsInBM
    if BM['image'] == 'pyimage1':
        WhatsInBM = 'O'
    else:
        if BM['image'] == 'pyimage2':
            WhatsInBM = 'X'
def SeeWhatsInBR():
    global WhatsInBR
    if BR['image'] == 'pyimage1':
        WhatsInBR = 'O'
    else:
        if BR['image'] == 'pyimage2':
            WhatsInBR = 'X'

# This is going to check if all buttons have been clicked and are disabled
def AllDisabled():
    global IsDisabled
    if TL['state'] == DISABLED:
        if TM['state'] == DISABLED:
            if TR['state'] == DISABLED:
                if ML['state'] == DISABLED:
                    if MM['state'] == DISABLED:
                        if MR['state'] == DISABLED:
                            if BL['state'] == DISABLED:
                                if BM['state'] == DISABLED:
                                    if BR['state'] == DISABLED:
                                        IsDisabled = 'True'
# This will disable all buttons when called
def DisableAll():
    TL['state'] = DISABLED
    TM['state'] = DISABLED
    TR['state'] = DISABLED
    ML['state'] = DISABLED
    MM['state'] = DISABLED
    MR['state'] = DISABLED
    BL['state'] = DISABLED
    BM['state'] = DISABLED
    BR['state'] = DISABLED

# This will enable all buttons when clicked
def EnableAll():
    TL['state'] = NORMAL
    TM['state'] = NORMAL
    TR['state'] = NORMAL
    ML['state'] = NORMAL
    MM['state'] = NORMAL
    MR['state'] = NORMAL
    BL['state'] = NORMAL
    BM['state'] = NORMAL
    BR['state'] = NORMAL

# Reset button
def Reset():
    global WhatsInTL
    global WhatsInTM
    global WhatsInTR
    global WhatsInML
    global WhatsInMM
    global WhatsInMR
    global WhatsInBL
    global WhatsInBM
    global WhatsInBR
    global WhosTurn
    global IsDisabled
    global WinnerFound
    TL['image'] = StartingImage
    TM['image'] = StartingImage
    TR['image'] = StartingImage
    ML['image'] = StartingImage
    MM['image'] = StartingImage
    MR['image'] = StartingImage
    BL['image'] = StartingImage
    BM['image'] = StartingImage
    BR['image'] = StartingImage
    WhatsInTL = '-'
    WhatsInTM = '-'
    WhatsInTR = '-'
    WhatsInML = '-'
    WhatsInMM = '-'
    WhatsInMR = '-'
    WhatsInBL = '-'
    WhatsInBM = '-'
    WhatsInBR = '-'
    WhosTurn = 'X'
    WhosTurnLabel['text'] = "It's " + WhosTurn + "'s turn."
    EnableAll()
    WinnerFound = 'False'
    IsDisabled = 'False'

# This will find who the winner is
def WinnerO():
    global WhosTurnLabel
    global IsDisabled
    global WinnerFound
    if WhatsInTL == 'O':
        if WhatsInTM == 'O':
            if WhatsInTR == 'O':
                WhosTurnLabel['text'] = 'O is the winner!!!'
                DisableAll()
                WinnerFound = 'True'
    if WhatsInML == 'O':
        if WhatsInMM == 'O':
            if WhatsInMR == 'O':
                WhosTurnLabel['text'] = 'O is the winner!!!'
                DisableAll()
                WinnerFound = 'True'
    if WhatsInBL == 'O':
        if WhatsInBM == 'O':
            if WhatsInBR == 'O':
                WhosTurnLabel['text'] = 'O is the winner!!!'
                DisableAll()
                WinnerFound = 'True'
    if WhatsInTL == 'O':
        if WhatsInML == 'O':
            if WhatsInBR == 'O':
                WhosTurnLabel['text'] = 'O is the winner!!!'
                DisableAll()
                WinnerFound = 'True'
    if WhatsInTR == 'O':
        if WhatsInMR == 'O':
            if WhatsInBR == 'O':
                WhosTurnLabel['text'] = 'O is the winner!!!'
                DisableAll()
                WinnerFound = 'True'
    if WhatsInTM == 'O':
        if WhatsInMM == 'O':
            if WhatsInBM == 'O':
                WhosTurnLabel['text'] = 'O is the winner!!!'
                DisableAll()
                WinnerFound = 'True'
    if WhatsInTL == 'O':
        if WhatsInMM == 'O':
            if WhatsInBR == 'O':
                WhosTurnLabel['text'] = 'O is the winner!!!'
                DisableAll()
                WinnerFound = 'True'
    if WhatsInTR == 'O':
        if WhatsInMM == 'O':
            if WhatsInBL == 'O':
                WhosTurnLabel['text'] = 'O is the winner!!!'
                DisableAll()
                WinnerFound = 'True'
def WinnerX():
    global WhosTurnLabel
    global IsDisabled
    global WinnerFound
    if WhatsInTL == 'X':
        if WhatsInTM == 'X':
            if WhatsInTR == 'X':
                WhosTurnLabel['text'] = 'X is the winner!!!'
                DisableAll()
                WinnerFound = 'True'
    if WhatsInML == 'X':
        if WhatsInMM == 'X':
            if WhatsInMR == 'X':
                WhosTurnLabel['text'] = 'X is the winner!!!'
                DisableAll()
                WinnerFound = 'True'
    if WhatsInBL == 'X':
        if WhatsInBM == 'X':
            if WhatsInBR == 'X':
                WhosTurnLabel['text'] = 'X is the winner!!!'
                DisableAll()
                WinnerFound = 'True'
    if WhatsInTL == 'X':
        if WhatsInML == 'X':
            if WhatsInBL == 'X':
                WhosTurnLabel['text'] = 'X is the winner!!!'
                DisableAll()
                WinnerFound = 'True'
    if WhatsInTR == 'X':
        if WhatsInMR == 'X':
            if WhatsInBR == 'X':
                WhosTurnLabel['text'] = 'X is the winner!!!'
                DisableAll()
                WinnerFound = 'True'
    if WhatsInTM == 'X':
        if WhatsInMM == 'X':
            if WhatsInBM == 'X':
                WhosTurnLabel['text'] = 'X is the winner!!!'
                DisableAll()
                WinnerFound = 'True'
    if WhatsInTL == 'X':
        if WhatsInMM == 'X':
            if WhatsInBR == 'X':
                WhosTurnLabel['text'] = 'X is the winner!!!'
                DisableAll()
                WinnerFound = 'True'
    if WhatsInTR == 'X':
        if WhatsInMM == 'X':
            if WhatsInBL == 'X':
                WhosTurnLabel['text'] = 'X is the winner!!!'
                DisableAll()
                WinnerFound = 'True'
def Tie():
    global WinnerFound
    if WinnerFound == 'False':
        if IsDisabled == 'True':
            WhosTurnLabel['text'] = "It's a tie!!!"

# This changes the label at the bottom and displays whos turn it is.
def ChangeWhosTurnLabel(): 
    WhosTurnLabel['text'] = "It's " + WhosTurn + "'s turn."

# Background color and placeholder for the size
background = Canvas(width='500', height='500', bg='#9EADC8')
background.pack()

# Label for whos turn it is
WhosTurnLabel = Label(text= "It's " + WhosTurn + "'s turn.")
WhosTurnLabel.pack()
# BoardImage
boardimage = PhotoImage(file='TikTacToe.png')
background.create_image(250, 250, image=boardimage,)

# Buttons that display X/O depending on whos turn when clicked
TL = Button(command=lambda: [DisableTL(), NextTurn(), ChangeImageTL(), ChangeWhosTurnLabel(), SeeWhatsInTL(), WinnerO(), WinnerX(), AllDisabled(), Tie()], image=StartingImage, width='90', height='90', bg='#9EADC8', activebackground='#9eadc8', borderwidth=0,)
TL.place(relx=0.19, rely=0.18)
TM = Button(command=lambda: [DisableTM(), NextTurn(), ChangeImageTM(), ChangeWhosTurnLabel(), SeeWhatsInTM(), WinnerO(), WinnerX(), AllDisabled(), Tie()], image=StartingImage, width='90', height='90', bg='#9EADC8', activebackground='#9eadc8', borderwidth=0)
TM.place(relx=0.4, rely=0.18)
TR = Button(command=lambda: [DisableTR(), NextTurn(), ChangeImageTR(), ChangeWhosTurnLabel(), SeeWhatsInTR(), WinnerO(), WinnerX(), AllDisabled(), Tie()], image=StartingImage, width='90', height='90', bg='#9EADC8', activebackground='#9eadc8', borderwidth=0)
TR.place(relx=0.61, rely=0.18)
ML = Button(command=lambda: [DisableML(), NextTurn(), ChangeImageML(), ChangeWhosTurnLabel(), SeeWhatsInML(), WinnerO(), WinnerX(), AllDisabled(), Tie()], image=StartingImage, width='90', height='90', bg='#9EADC8', activebackground='#9eadc8', borderwidth=0)
ML.place(relx=0.19, rely=0.38)
MM = Button(command=lambda: [DisableMM(), NextTurn(), ChangeImageMM(), ChangeWhosTurnLabel(), SeeWhatsInMM(), WinnerO(), WinnerX(), AllDisabled(), Tie()], image=StartingImage, width='90', height='90', bg='#9EADC8', activebackground='#9eadc8', borderwidth=0)
MM.place(relx=0.4, rely=0.38)
MR = Button(command=lambda: [DisableMR(), NextTurn(), ChangeImageMR(), ChangeWhosTurnLabel(), SeeWhatsInMR(), WinnerO(), WinnerX(), AllDisabled(), Tie()], image=StartingImage, width='90', height='90', bg='#9EADC8', activebackground='#9eadc8', borderwidth=0)
MR.place(relx=0.61, rely=0.38)
BL = Button(command=lambda: [DisableBL(), NextTurn(), ChangeImageBL(), ChangeWhosTurnLabel(), SeeWhatsInBL(), WinnerO(), WinnerX(), AllDisabled(), Tie()], image=StartingImage, width='90', height='90', bg='#9EADC8', activebackground='#9eadc8', borderwidth=0)
BL.place(relx=0.19, rely=0.59)
BM = Button(command=lambda: [DisableBM(), NextTurn(), ChangeImageBM(), ChangeWhosTurnLabel(), SeeWhatsInBM(), WinnerO(), WinnerX(), AllDisabled(), Tie()], image=StartingImage, width='90', height='90', bg='#9EADC8', activebackground='#9eadc8', borderwidth=0)
BM.place(relx=0.4, rely=0.59)
BR = Button(command=lambda: [DisableBR(), NextTurn(), ChangeImageBR(), ChangeWhosTurnLabel(), SeeWhatsInBR(), WinnerO(), WinnerX(), AllDisabled(), Tie()], image=StartingImage, width='90', height='90', bg='#9EADC8', activebackground='#9eadc8', borderwidth=0)
BR.place(relx=0.618, rely=0.59)

ResetButton = Button(text='Reset', bg='#9EADC8', activebackground='#9eadc8', command = Reset)
ResetButton.place(relx=0.45, rely=0.9)

root.mainloop()