import tkinter as tk
from tkinter.font import BOLD
import winsound
root = tk.Tk()
root.geometry('1300x700')
frame = tk.Frame()
frame.master.title('Click and Change')
canvas = tk.Canvas(frame)
root.resizable(0,0)
# ------img------------
charactor=tk.PhotoImage(file="img/character.png")
wall=tk.PhotoImage(file="img/wall.png")
ghost1=tk.PhotoImage(file="img/ghost1.png")
ghost2=tk.PhotoImage(file="img/ghost2.png")
door=tk.PhotoImage(file="img/door.png")
key1 = tk.PhotoImage(file='img/key.png')
lost=tk.PhotoImage(file="img/lost.png")
win=tk.PhotoImage(file='img/win.png')
bg = tk.PhotoImage(file='img/background1.png')
bg2 = tk.PhotoImage(file='img/f_background.png')
bgGame=tk.PhotoImage(file='img/snow-background.png')
def start(event):
    canvas.delete('all')
    canvas.create_image(0, 0, image=bg2, anchor='nw')
    canvas.create_rectangle(620, 345, 760, 400, fill="green",outline='', tags='start')
    canvas.create_text(690, 370,text='START', fill="white", font=('Purisa', 25), tags='start')
    canvas.create_text(690, 300,text='Christmas Day!', fill="white", font=('Purisa', 40,BOLD), tags='start')
    
def chooseLevel(event):
    winsound.PlaySound("sounds/startGame.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
    canvas.delete('all')
    canvas.create_image(0, 0, image=bg, anchor='nw')
    # Button for click go back
    canvas.create_rectangle(20, 55, 140, 85, fill="green",outline='', tags='back')
    canvas.create_text(70, 70,text='BACK', fill="white", font=('Purisa', 15), tags='back')
    # Button for click to level 1
    canvas.create_oval(350, 300, 450, 400, fill='blue', tags='level-1')
    canvas.create_text(400, 350,text='easy', fill="white", font=('Purisa', 20), tags='level-1')
    # Button for click to level 2
    canvas.create_oval(500, 300, 600, 400, fill='red', tags='level-2')
    canvas.create_text(550, 350,text='menuim', fill="white", font=('Purisa', 20), tags='level-2')

    # Button for click to level 3
    canvas.create_oval(650, 300, 750, 400, fill='gold', tags='level-3')
    canvas.create_text(700, 350,text='hard', fill="white", font=('Purisa', 20), tags='level-3')

    
# ============================================Start Game=========================================
checkForMonsterMove = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
checkForStopCode = True
sontaHaskey = False
number = 0
numberComp = 0
level1 = False
level2 = False
level3 = False
level4 = False
level5 = Falsearray2D = []

# move item to left 
def charactorMoveLeft(event):
    moveCharactor(0, -1)
# move item to right
def charactorMoveRight(event):
    moveCharactor(0, 1)
# move item to down
def charactorMoveDown(event):
    moveCharactor(1, 0)
# move item to up
def charactorMoveUp(event):
    moveCharactor(-1, 0)


# -------------------------------------level 2--------------------------------------------



# find index of monster



def level_1(event):
    global array2D, numberComp, level1, checkForStopCode
    checkForStopCode = True
    level1 = True
    numberComp = 1
    array2D =     [[7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
                    [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 7],
                    [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
                    [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
                    [7, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 7, 7, 7],
                    [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
                    [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
                    [7, 0, 0, 0, 0, 0, 0, 0, 0, 24, 0, 0, 25, 7, 7, 7, 7, 7, 7, 7], 
                    [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 26, 7], 
                    [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]]
    findIndexOfMonster()

def level_2(event):
    global array2D, numberComp, level2, checkForStopCode
    checkForStopCode = True
    level2 = True
    numberComp = 14
    array2D =   [[7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
                [7, 1, 0, 0, 0, 0, 0, 0, 5, 0, 0, 7, 0, 0, 0, 9, 0, 0, 0, 7],
                [7, 0, 14, 7, 7, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
                [7, 2, 0, 0, 7, 25, 0, 7, 0, 0, 15, 0, 7, 8, 3, 0, 0, 0, 0, 7],
                [7, 0, 0, 0, 7, 0, 0, 7, 7, 7, 7, 7, 6, 7, 7, 7, 13, 7, 7, 7],
                [7, 11, 0, 0, 7, 0, 10, 0, 7, 0, 0, 12, 0, 0, 0, 0, 0, 0, 0, 7],
                [7, 0, 0, 0, 7, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
                [7, 0, 0, 0, 7, 7, 0, 0, 7, 24, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7], 
                [7, 4, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 26, 7], 
                [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]]
                   
    findIndexOfMonster()

def level_3(event):
    global array2D, numberComp, level3, checkForStopCode
    checkForStopCode = True
    level3 = True
    numberComp = 10
    array2D=[[7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
            [7, 26, 24, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
            [7, 7, 7, 5, 7, 7, 7, 0, 10, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 7],
            [7, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 0, 7, 0, 0, 0, 0, 0, 2, 7],
            [7, 9, 0, 0, 0, 0, 0, 7, 7, 0, 7, 7, 0, 7, 7, 7, 7, 7, 0, 7],
            [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 7],
            [7, 0, 7, 7, 7, 7, 6, 7, 7, 7, 7, 7, 0, 7, 7, 7, 7, 7, 7, 7],
            [7, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7], 
            [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 25, 7], 
            [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]]
    findIndexOfMonster()

# For user click and play again
def doublePlays(event):
    findIndexOfMonster()
# check number of moster for move
def numberOfMonsterMove():
    global number
    if number < numberComp:
        number += 1
    else:
        number = 1
    
    if number == 7:
        number += 1
    return number
# find array of indext of monster stand on
def findIndexOfMonster():
    index = numberOfMonsterMove()
    for col in range(len(array2D)):
        for row in range(len(array2D[col])):
            if array2D[col][row] == index:
                arrayOfMonsterStandOn = col
    # index of monster move to left and right
    if index <= 4:   
        moveMonsters(arrayOfMonsterStandOn, index, 1, 1, 0, 0)
    # index of monster move to Up and down   
    if 15> index > 4:
        moveMonsters(arrayOfMonsterStandOn, index, 0, 0, 1, 1)
    else: 
        findIndexOfMonster
# create grid of game
def createGrid():
    canvas.delete('all')
    canvas.create_image(700,300, image=bgGame)
    size = 1200 / len(array2D[0])
    y1 = size
    y2 = size*2
    for key in array2D:
        x1 = 40 
        x2 = x1+size
        for v in key:
            if v == 7 :
                canvas.create_image(x1,y1, image=wall ,anchor="nw")
            if v == 1:
                canvas.create_image(x1,y1, image=ghost1 ,anchor="nw")
            if v == 2:
                canvas.create_image(x1,y1, image=ghost1 ,anchor="nw")
            if v == 3:
                canvas.create_image(x1,y1, image=ghost1 ,anchor="nw")
            if v == 4:
                canvas.create_image(x1,y1, image=ghost1 ,anchor="nw")
            if v == 5:
                canvas.create_image(x1,y1, image=ghost1 ,anchor="nw")
            if v == 6:
                canvas.create_image(x1,y1, image=ghost1 ,anchor="nw")
            if v == 8:
                canvas.create_image(x1,y1, image=ghost1 ,anchor="nw")
            if v == 9:
                canvas.create_image(x1,y1, image=ghost1 ,anchor="nw")
            if v == 10:
                canvas.create_image(x1,y1, image=ghost1 ,anchor="nw")
            if v == 11:
                canvas.create_image(x1,y1, image=ghost1 ,anchor="nw")
            if v == 12:
                canvas.create_image(x1,y1, image=ghost1 ,anchor="nw")
            if v == 13:
                canvas.create_image(x1,y1, image=ghost1 ,anchor="nw")
            if v == 14:
                canvas.create_image(x1,y1, image=ghost1 ,anchor="nw")
            if v == 15:
                canvas.create_image(x1,y1, image=ghost1 ,anchor="nw")
            if v == 16:
                canvas.create_image(x1,y1, image=ghost1 ,anchor="nw")
            if v == 17:
                canvas.create_image(x1,y1, image=ghost1 ,anchor="nw")
            if v == 18:
                canvas.create_image(x1,y1, image=ghost1 ,anchor="nw")
            if v == 19:
                canvas.create_image(x1,y1, image=ghost1 ,anchor="nw")
            if v == 20:
                canvas.create_image(x1,y1, image=ghost1 ,anchor="nw")
            if v == 21:
                canvas.create_image(x1,y1, image=ghost1 ,anchor="nw")
            if v == 22:
                canvas.create_image(x1,y1, image=ghost1 ,anchor="nw")
            if v == 23:
                canvas.create_image(x1,y1, image=ghost1 ,anchor="nw")
            if v == 24:
                canvas.create_image(x1,y1, image=charactor ,anchor="nw")
            if v == 25:
                canvas.create_image(x1,y1, image=key1 ,anchor="nw")
            if v == 26:
                canvas.create_image(x1,y1, image=door ,anchor="nw")
            else:
                canvas.create_rectangle(x1, y1, x2, y2,fill="",outline="")
            x1 += size
            x2 += size
        y1 += size
        y2 += size
# get to move to left right up and down
def moveMonsters(arrayOfMonsterStandOn, index, left, right, up, down):
    global  checkForMonsterMove, checkForStopCode
    if checkForStopCode:
        for i in range(len(array2D[arrayOfMonsterStandOn])):
                times = 1
                if array2D[arrayOfMonsterStandOn][i] == index:                    
                    # get move to right and move to down
                    if array2D[arrayOfMonsterStandOn+down][i+right] == 0 and not checkForMonsterMove[index]:
                        array2D[arrayOfMonsterStandOn][i] = 0
                        array2D[arrayOfMonsterStandOn+down][i+right] = index
                    elif array2D[arrayOfMonsterStandOn+down][i+right] == 24:
                        array2D[arrayOfMonsterStandOn][i] = 0
                        array2D[arrayOfMonsterStandOn+down][i+right] = index
                        checkForStopCode = False
                        break
                    elif array2D[arrayOfMonsterStandOn+down][i+right] == 7 and not checkForMonsterMove[index]:
                        checkForMonsterMove[index] = True
                        times = 0
                    # get move to left and move to up
                    elif  array2D[arrayOfMonsterStandOn-up][i-left] == 0 and checkForMonsterMove[index]:
                        array2D[arrayOfMonsterStandOn][i] = 0
                        array2D[arrayOfMonsterStandOn-up][i-left] = index
                    elif array2D[arrayOfMonsterStandOn-up][i-left] == 24:
                        array2D[arrayOfMonsterStandOn][i] = 0
                        array2D[arrayOfMonsterStandOn-up][i-left] = index
                        checkForStopCode = False
                        break
                    elif array2D[arrayOfMonsterStandOn-up][i-left] == 7 and checkForMonsterMove[index]:
                        times = 0
                        checkForMonsterMove[index] = False
                    break
        if checkForStopCode:
            createGrid()
            canvas.after(times, findIndexOfMonster)
        else:
            gameLost()
# move Charactor to left right up and down
def moveCharactor(index1, index2):
    global  checkForStopCode, sontaHaskey
    checkForStopLoop = True
    if checkForStopCode:
        for v in range(len(array2D)):
            for i in range(len(array2D[v])):
                if array2D[v][i] == 24 and checkForStopLoop:
                    if array2D[v+(index1)][i+(index2)] == 0:
                            array2D[v+(index1)][i+index2] = 24
                            array2D[v][i] = 0
                    elif array2D[v+(index1)][i+(index2)]==7:
                            array2D[v][i] =24
                    # Check for game lost
                    elif array2D[v+(index1)][i+(index2)]!=26 and array2D[v+(index1)][i+(index2)]!=25:
                            checkForStopCode = False
                            array2D[v][i]=0
                            gameLost()
                    elif array2D[v+(index1)][i+(index2)]==25:
                            array2D[v+(index1)][i+index2] = 24
                            array2D[v][i] = 0
                            sontaHaskey = True
                            winsound.PlaySound("sounds/getKey.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
                            
                    # check for game win
                    elif array2D[v+(index1)][i+(index2)]==26 and sontaHaskey:
                            array2D[v+(index1)][i+index2] = 24
                            array2D[v][i] = 0
                            gameWin()
                            winsound.PlaySound("sounds/gameWin.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
                            checkForStopCode = False
                    checkForStopLoop = False
        if checkForStopCode:
            createGrid()
def continueGame():
    global  checkForMonsterMove, checkForStopCode, sontaHaskey, number, array2D
    canvas.create_text(650, 350,text='Whould you like to continue the Game!', fill="red", font=('Purisa', 30))
    canvas.create_rectangle(450, 490, 580, 550, fill='blue', tags='continuegame')
    canvas.create_text(515, 520,text='YES', fill="white", font=('Purisa', 35), tags='continuegame')
    checkForMonsterMove = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
    sontaHaskey = False
    number = 0
    canvas.after(0, rexitGame)
    if level1:
        canvas.tag_bind('continuegame', '<Button-1>', level_1)
    if level2:
        canvas.tag_bind('continuegame', '<Button-1>', level_2)
    if level3:
        canvas.tag_bind('continuegame', '<Button-1>', level_3)

def rexitGame():
    canvas.create_rectangle(640, 490, 760, 550, fill='blue', tags='noContinuegame')
    canvas.create_text(700, 520,text='NO', fill="white", font=('Purisa', 35), tags='noContinuegame')
    canvas.create_text(100, 40,text='<<Back to menu', fill="white", font=('Purisa', 18), tags='noContinuegame')
    canvas.tag_bind('noContinuegame', '<Button-1>', chooseLevel)

    
# -------next level------
def nextLevel():
    global  checkForMonsterMove, checkForStopCode, sontaHaskey, number, array2D
    canvas.delete('all')
    createGrid()
    canvas.create_image(250,250, image=win ,anchor="nw")
    canvas.create_rectangle(640, 490, 760, 550, fill='blue', tags='noContinuegame')
    canvas.create_text(700, 520,text='EXIT', fill="white", font=('Purisa', 30), tags='noContinuegame')
    # --play again--
    canvas.create_rectangle(450, 490, 580, 550, fill='blue', tags='continuegame')
    canvas.create_text(515, 520,text='AGAIN', fill="white", font=('Purisa', 30), tags='continuegame')
    # --back to level--
    canvas.create_text(100, 40,text='<<Back to menu', fill="white", font=('Purisa', 20), tags='noContinueLevel2')
    canvas.create_rectangle(800, 490, 920, 550, fill='blue', tags='nextLevel')
    canvas.create_text(860, 520,text='NEXT', fill="white", font=('Purisa', 30), tags='nextLevel')
    # canvas.after(0, continueGame)
    checkForMonsterMove = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
    # checkForStopCode = True
    sontaHaskey = False
    number = 0
    canvas.tag_bind('nextLevel', '<Button-1>', chooseLevel)
    if level1:
        canvas.tag_bind('nextLevel', '<Button-1>', level_2)
    if level2:
        canvas.tag_bind('nextLevel', '<Button-1>', level_3)
# -----lost---
def gameLost():
    createGrid()  
    winsound.PlaySound("sounds/Lost.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
    canvas.create_image(250,250, image=lost ,anchor="nw")
    canvas.after(0, continueGame)
# ---- win-----
def gameWin():
    createGrid()
    canvas.create_image(250,250, image=win ,anchor="nw")
    canvas.create_text(100, 40,text='<<Back to menu', fill="white", font=('Purisa', 20), tags='noContinueLevel2')
    canvas.after(500, nextLevel)
    winsound.PlaySound("sounds/gameWin.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

start(event=start)
# ---button to move player--
if checkForStopCode:
    root.bind('<a>', charactorMoveLeft)
    root.bind('<d>', charactorMoveRight)
    root.bind('<w>', charactorMoveUp)
    root.bind('<s>', charactorMoveDown)
    root.bind('<Left>', charactorMoveLeft)
    root.bind('<Right>', charactorMoveRight)
    root.bind('<Up>', charactorMoveUp)
    root.bind('<Down>', charactorMoveDown)
#---- button menu and level----
canvas.tag_bind('noContinuegame', '<Button-1>', chooseLevel)
canvas.tag_bind('continuegame', '<Button-1>', doublePlays)
canvas.tag_bind('back', '<Button-1>', start)
canvas.tag_bind('start', '<Button-1>', chooseLevel)
canvas.tag_bind('level-1', '<Button-1>', level_1)
canvas.tag_bind('level-2', '<Button-1>', level_2)
canvas.tag_bind('level-3', '<Button-1>', level_3)
canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')
root.mainloop()