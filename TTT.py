from tkinter import *
import tkinter as tk
from array import *



PlayedTurns = 0
Player1Turn = 1
Player2Turn = 0
BlockColors = [0,0,0,0,0,0,0,0,0]

master = Tk()

frame = Frame(master, width=301, height=350)
frame.pack()
                    
def ButTop1() :
    global Player1Turn
    global Player2Turn
    global BlockColors
    if (Player1Turn == 1 and Player2Turn == 0) :
        Button(master, text="", bg="blue").place(x = 1, y = 1, width=99, height=99)
        Player1Turn = 0
        Player2Turn = 1
        BlockColors[0] = 1
        Button(master, text="Player 2's Turn", bg="red", fg="white").place(x = 101, y = 301, width=99, height=49)
        WinCheck()
    elif (Player1Turn == 0 and Player2Turn == 1) :  
        Button(master, text="", bg="red").place(x = 1, y = 1, width=99, height=99)
        Player1Turn = 1
        Player2Turn = 0
        BlockColors[0] = 2
        Button(master, text="Player 1's Turn", bg="blue", fg="white").place(x = 101, y = 301, width=99, height=49)
        WinCheck()

def ButTop2() :
    global Player1Turn
    global Player2Turn
    global BlockColors
    if (Player1Turn == 1 and Player2Turn == 0) :
        Button(master, text="", bg="blue").place(x = 101, y = 1, width=99, height=99)
        Player1Turn = 0
        Player2Turn = 1
        BlockColors[1] = 1
        Button(master, text="Player 2's Turn", bg="red", fg="white").place(x = 101, y = 301, width=99, height=49)
        WinCheck()
    elif (Player1Turn == 0 and Player2Turn == 1) :  
        Button(master, text="", bg="red").place(x = 101, y = 1, width=99, height=99)
        Player1Turn = 1
        Player2Turn = 0
        BlockColors[1] = 2
        Button(master, text="Player 1's Turn", bg="blue", fg="white").place(x = 101, y = 301, width=99, height=49)
        WinCheck()

def ButTop3() :
    global Player1Turn
    global Player2Turn
    global BlockColors
    if (Player1Turn == 1 and Player2Turn == 0) :
        Button(master, text="", bg="blue").place(x = 201, y = 1, width=99, height=99)
        Player1Turn = 0
        Player2Turn = 1
        BlockColors[2] = 1
        Button(master, text="Player 2's Turn", bg="red", fg="white").place(x = 101, y = 301, width=99, height=49)
        WinCheck()
    elif (Player1Turn == 0 and Player2Turn == 1) :  
        Button(master, text="", bg="red").place(x = 201, y = 1, width=99, height=99)
        Player1Turn = 1
        Player2Turn = 0
        BlockColors[2] = 2
        Button(master, text="Player 1's Turn", bg="blue", fg="white").place(x = 101, y = 301, width=99, height=49)
        WinCheck()

def ButMid1() :
    global Player1Turn
    global Player2Turn
    global BlockColors
    if (Player1Turn == 1 and Player2Turn == 0) :
        Button(master, text="", bg="blue").place(x = 1, y = 101, width=99, height=99)
        Player1Turn = 0
        Player2Turn = 1
        BlockColors[3] = 1
        Button(master, text="Player 2's Turn", bg="red", fg="white").place(x = 101, y = 301, width=99, height=49)
        WinCheck()
    elif (Player1Turn == 0 and Player2Turn == 1) :  
        Button(master, text="", bg="red").place(x = 1, y = 101, width=99, height=99)
        Player1Turn = 1
        Player2Turn = 0
        BlockColors[3] = 2
        Button(master, text="Player 1's Turn", bg="blue", fg="white").place(x = 101, y = 301, width=99, height=49)
        WinCheck()

def ButMid2() :
    global Player1Turn
    global Player2Turn
    global BlockColors
    if (Player1Turn == 1 and Player2Turn == 0) :
        Button(master, text="", bg="blue").place(x = 101, y = 101, width=99, height=99)
        Player1Turn = 0
        Player2Turn = 1
        BlockColors[4] = 1
        Button(master, text="Player 2's Turn", bg="red", fg="white").place(x = 101, y = 301, width=99, height=49)
        WinCheck()
    elif (Player1Turn == 0 and Player2Turn == 1) :  
        Button(master, text="", bg="red").place(x = 101, y = 101, width=99, height=99)
        Player1Turn = 1
        Player2Turn = 0
        BlockColors[4] = 2
        Button(master, text="Player 1's Turn", bg="blue", fg="white").place(x = 101, y = 301, width=99, height=49)
        WinCheck()

def ButMid3() :
    global Player1Turn
    global Player2Turn
    global BlockColors
    if (Player1Turn == 1 and Player2Turn == 0) :
        Button(master, text="", bg="blue").place(x = 201, y = 101, width=99, height=99)
        Player1Turn = 0
        Player2Turn = 1
        BlockColors[5] = 1
        Button(master, text="Player 2's Turn", bg="red", fg="white").place(x = 101, y = 301, width=99, height=49)
        WinCheck()
    elif (Player1Turn == 0 and Player2Turn == 1) :  
        Button(master, text="", bg="red").place(x = 201, y = 101, width=99, height=99)
        Player1Turn = 1
        Player2Turn = 0
        BlockColors[5] = 2
        Button(master, text="Player 1's Turn", bg="blue", fg="white").place(x = 101, y = 301, width=99, height=49)
        WinCheck()

def ButBot1() :
    global Player1Turn
    global Player2Turn
    global BlockColors
    if (Player1Turn == 1 and Player2Turn == 0) :
        Button(master, text="", bg="blue").place(x = 1, y = 201, width=99, height=99)
        Player1Turn = 0
        Player2Turn = 1
        BlockColors[6] = 1
        Button(master, text="Player 2's Turn", bg="red", fg="white").place(x = 101, y = 301, width=99, height=49)
        WinCheck()
    elif (Player1Turn == 0 and Player2Turn == 1) :  
        Button(master, text="", bg="red").place(x = 1, y = 201, width=99, height=99)
        Player1Turn = 1
        Player2Turn = 0
        BlockColors[6] = 2
        Button(master, text="Player 1's Turn", bg="blue", fg="white").place(x = 101, y = 301, width=99, height=49)
        WinCheck()

def ButBot2() :
    global Player1Turn
    global Player2Turn
    global BlockColors
    if (Player1Turn == 1 and Player2Turn == 0) :
        Button(master, text="", bg="blue").place(x = 101, y = 201, width=99, height=99)
        Player1Turn = 0
        Player2Turn = 1
        BlockColors[7] = 1
        Button(master, text="Player 2's Turn", bg="red", fg="white").place(x = 101, y = 301, width=99, height=49)
        WinCheck()
    elif (Player1Turn == 0 and Player2Turn == 1) :  
        Button(master, text="", bg="red").place(x = 101, y = 201, width=99, height=99)
        Player1Turn = 1
        Player2Turn = 0
        BlockColors[7] = 2
        Button(master, text="Player 1's Turn", bg="blue", fg="white").place(x = 101, y = 301, width=99, height=49)
        WinCheck()

def ButBot3() :
    global Player1Turn
    global Player2Turn
    global BlockColors
    if (Player1Turn == 1 and Player2Turn == 0) :
        Button(master, text="", bg="blue").place(x = 201, y = 201, width=99, height=99)
        Player1Turn = 0
        Player2Turn = 1
        BlockColors[8] = 1
        Button(master, text="Player 2's Turn", bg="red", fg="white").place(x = 101, y = 301, width=99, height=49)
        WinCheck()
    elif (Player1Turn == 0 and Player2Turn == 1) :  
        Button(master, text="", bg="red").place(x = 201, y = 201, width=99, height=99)
        Player1Turn = 1
        Player2Turn = 0
        BlockColors[8] = 2
        Button(master, text="Player 1's Turn", bg="blue", fg="white").place(x = 101, y = 301, width=99, height=49)
        WinCheck()

def Finished3x3() :
    if (BlockColors[0] == 0) :
        Label(master, text="", bg="white").place(x = 101, y = 201, width=33, height=33)
    if (BlockColors[0] == 1) :
        Label(master, text="", bg="blue").place(x = 101, y = 201, width=33, height=33)
    if (BlockColors[0] == 2) :
        Label(master, text="", bg="red").place(x = 101, y = 201, width=33, height=33)
    if (BlockColors[1] == 0) :
        Label(master, text="", bg="white").place(x = 134, y = 201, width=33, height=33)
    if (BlockColors[1] == 1) :
        Label(master, text="", bg="blue").place(x = 134, y = 201, width=33, height=33)
    if (BlockColors[1] == 2) :
        Label(master, text="", bg="red").place(x = 134, y = 201, width=33, height=33)
    if (BlockColors[2] == 0) :
        Label(master, text="", bg="white").place(x = 167, y = 201, width=33, height=33)
    if (BlockColors[2] == 1) :
        Label(master, text="", bg="blue").place(x = 167, y = 201, width=33, height=33)
    if (BlockColors[2] == 2) :
        Label(master, text="", bg="red").place(x = 167, y = 201, width=33, height=33)
    if (BlockColors[3] == 0) :
        Label(master, text="", bg="white").place(x = 101, y = 234, width=33, height=33)
    if (BlockColors[3] == 1) :
        Label(master, text="", bg="blue").place(x = 101, y = 234, width=33, height=33)
    if (BlockColors[3] == 2) :
        Label(master, text="", bg="red").place(x = 101, y = 234, width=33, height=33)
    if (BlockColors[4] == 0) :
        Label(master, text="", bg="white").place(x = 134, y = 234, width=33, height=33)
    if (BlockColors[4] == 1) :
        Label(master, text="", bg="blue").place(x = 134, y = 234, width=33, height=33)
    if (BlockColors[4] == 2) :
        Label(master, text="", bg="red").place(x = 134, y = 234, width=33, height=33)
    if (BlockColors[5] == 0) :
        Label(master, text="", bg="white").place(x = 167, y = 234, width=33, height=33)
    if (BlockColors[5] == 1) :
        Label(master, text="", bg="blue").place(x = 167, y = 234, width=33, height=33)
    if (BlockColors[5] == 2) :
        Label(master, text="", bg="red").place(x = 167, y = 234, width=33, height=33)
    if (BlockColors[6] == 0) :
        Label(master, text="", bg="white").place(x = 101, y = 267, width=33, height=33)
    if (BlockColors[6] == 1) :
        Label(master, text="", bg="blue").place(x = 101, y = 267, width=33, height=33)
    if (BlockColors[6] == 2) :
        Label(master, text="", bg="red").place(x = 101, y = 267, width=33, height=33)
    if (BlockColors[7] == 0) :
        Label(master, text="", bg="white").place(x = 134, y = 267, width=33, height=33)
    if (BlockColors[7] == 1) :
        Label(master, text="", bg="blue").place(x = 134, y = 267, width=33, height=33)
    if (BlockColors[7] == 2) :
        Label(master, text="", bg="red").place(x = 134, y = 267, width=33, height=33)
    if (BlockColors[8] == 0) :
        Label(master, text="", bg="white").place(x = 167, y = 267, width=33, height=33)
    if (BlockColors[8] == 1) :
        Label(master, text="", bg="blue").place(x = 167, y = 267, width=33, height=33)
    if (BlockColors[8] == 2) :
        Label(master, text="", bg="red").place(x = 167, y = 267, width=33, height=33)

def WinCheck() :
    global BlockColors
    if (BlockColors[0] == 1 and BlockColors[1] == 1 and BlockColors[2] == 1) :
        Label(master, text="Blue Wins", bg="white").place(x = 1, y = 1, width=299, height=199)
        Label(master, text="", bg="white").place(x = 1, y = 200, width=299, height=100)
        Label(master, text="", bg="blue").place(x = 101, y = 201, width=99, height=99)
        Button(master, text="Player 1 Wins", bg="blue", fg="white").place(x = 101, y = 301, width=99, height=49)
        Finished3x3()
        print ("Blue Wins")
    if (BlockColors[3] == 1 and BlockColors[4] == 1 and BlockColors[5] == 1) :
        Label(master, text="Blue Wins", bg="white").place(x = 1, y = 1, width=299, height=199)
        Label(master, text="", bg="white").place(x = 1, y = 200, width=299, height=100)
        Label(master, text="", bg="blue").place(x = 101, y = 201, width=99, height=99)
        Button(master, text="Player 1 Wins", bg="blue", fg="white").place(x = 101, y = 301, width=99, height=49)
        Finished3x3()
        print ("Blue Wins")
    if (BlockColors[6] == 1 and BlockColors[7] == 1 and BlockColors[8] == 1) :
        Label(master, text="Blue Wins", bg="white").place(x = 1, y = 1, width=299, height=199)
        Label(master, text="", bg="white").place(x = 1, y = 200, width=299, height=100)
        Label(master, text="", bg="blue").place(x = 101, y = 201, width=99, height=99)
        Button(master, text="Player 1 Wins", bg="blue", fg="white").place(x = 101, y = 301, width=99, height=49)
        Finished3x3()
        print ("Blue Wins")
    if (BlockColors[0] == 1 and BlockColors[3] == 1 and BlockColors[6] == 1) :
        Label(master, text="Blue Wins", bg="white").place(x = 1, y = 1, width=299, height=199)
        Label(master, text="", bg="white").place(x = 1, y = 200, width=299, height=100)
        Label(master, text="", bg="blue").place(x = 101, y = 201, width=99, height=99)
        Button(master, text="Player 1 Wins", bg="blue", fg="white").place(x = 101, y = 301, width=99, height=49)
        Finished3x3()
        print ("Blue Wins")
    if (BlockColors[1] == 1 and BlockColors[4] == 1 and BlockColors[7] == 1) :
        Label(master, text="Blue Wins", bg="white").place(x = 1, y = 1, width=299, height=199)
        Label(master, text="", bg="white").place(x = 1, y = 200, width=299, height=100)
        Label(master, text="", bg="blue").place(x = 101, y = 201, width=99, height=99)
        Button(master, text="Player 1 Wins", bg="blue", fg="white").place(x = 101, y = 301, width=99, height=49)
        Finished3x3()
        print ("Blue Wins")
    if (BlockColors[2] == 1 and BlockColors[5] == 1 and BlockColors[8] == 1) :
        Label(master, text="Blue Wins", bg="white").place(x = 1, y = 1, width=299, height=199)
        Label(master, text="", bg="white").place(x = 1, y = 200, width=299, height=100)
        Label(master, text="", bg="blue").place(x = 101, y = 201, width=99, height=99)
        Button(master, text="Player 1 Wins", bg="blue", fg="white").place(x = 101, y = 301, width=99, height=49)
        Finished3x3()
        print ("Blue Wins")
    if (BlockColors[0] == 1 and BlockColors[4] == 1 and BlockColors[8] == 1) :
        Label(master, text="Blue Wins", bg="white").place(x = 1, y = 1, width=299, height=199)
        Label(master, text="", bg="white").place(x = 1, y = 200, width=299, height=100)
        Label(master, text="", bg="blue").place(x = 101, y = 201, width=99, height=99)
        Button(master, text="Player 1 Wins", bg="blue", fg="white").place(x = 101, y = 301, width=99, height=49)
        Finished3x3()
        print ("Blue Wins")
    if (BlockColors[2] == 1 and BlockColors[4] == 1 and BlockColors[6] == 1) :
        Label(master, text="Blue Wins", bg="white").place(x = 1, y = 1, width=299, height=199)
        Label(master, text="", bg="white").place(x = 1, y = 200, width=299, height=100)
        Label(master, text="", bg="blue").place(x = 101, y = 201, width=99, height=99)
        Button(master, text="Player 1 Wins", bg="blue", fg="white").place(x = 101, y = 301, width=99, height=49)
        Finished3x3()
        print ("Blue Wins")

    if (BlockColors[0] == 2 and BlockColors[1] == 2 and BlockColors[2] == 2) :
        Label(master, text="Red Wins", bg="white").place(x = 1, y = 1, width=299, height=199)
        Label(master, text="", bg="white").place(x = 1, y = 200, width=299, height=100)
        Label(master, text="", bg="red").place(x = 101, y = 201, width=99, height=99)
        Button(master, text="Player 2 Wins", bg="red", fg="white").place(x = 101, y = 301, width=99, height=49)
        Finished3x3()
        print ("Red Wins")
    if (BlockColors[3] == 2 and BlockColors[4] == 2 and BlockColors[5] == 2) :
        Label(master, text="Red Wins", bg="white").place(x = 1, y = 1, width=299, height=199)
        Label(master, text="", bg="white").place(x = 1, y = 200, width=299, height=100)
        Label(master, text="", bg="red").place(x = 101, y = 201, width=99, height=99)
        Button(master, text="Player 2 Wins", bg="red", fg="white").place(x = 101, y = 301, width=99, height=49)
        Finished3x3()
        print ("Red Wins")
    if (BlockColors[6] == 2 and BlockColors[7] == 2 and BlockColors[8] == 2) :
        Label(master, text="Red Wins", bg="white").place(x = 1, y = 1, width=299, height=199)
        Label(master, text="", bg="white").place(x = 1, y = 200, width=299, height=100)
        Label(master, text="", bg="red").place(x = 101, y = 201, width=99, height=99)
        Button(master, text="Player 2 Wins", bg="red", fg="white").place(x = 101, y = 301, width=99, height=49)
        Finished3x3()
        print ("Red Wins")
    if (BlockColors[0] == 2 and BlockColors[3] == 2 and BlockColors[6] == 2) :
        Label(master, text="Red Wins", bg="white").place(x = 1, y = 1, width=299, height=199)
        Label(master, text="", bg="white").place(x = 1, y = 200, width=299, height=100)
        Label(master, text="", bg="red").place(x = 101, y = 201, width=99, height=99)
        Button(master, text="Player 2 Wins", bg="red", fg="white").place(x = 101, y = 301, width=99, height=49)
        Finished3x3()
        print ("Red Wins")
    if (BlockColors[1] == 2 and BlockColors[4] == 2 and BlockColors[7] == 2) :
        Label(master, text="Red Wins", bg="white").place(x = 1, y = 1, width=299, height=199)
        Label(master, text="", bg="white").place(x = 1, y = 200, width=299, height=100)
        Label(master, text="", bg="red").place(x = 101, y = 201, width=99, height=99)
        Button(master, text="Player 2 Wins", bg="red", fg="white").place(x = 101, y = 301, width=99, height=49)
        Finished3x3()
        print ("Red Wins")
    if (BlockColors[2] == 2 and BlockColors[5] == 2 and BlockColors[8] == 2) :
        Label(master, text="Red Wins", bg="white").place(x = 1, y = 1, width=299, height=199)
        Label(master, text="", bg="white").place(x = 1, y = 200, width=299, height=100)
        Label(master, text="", bg="red").place(x = 101, y = 201, width=99, height=99)
        Button(master, text="Player 2 Wins", bg="red", fg="white").place(x = 101, y = 301, width=99, height=49)
        Finished3x3()
        print ("Red Wins")
    if (BlockColors[0] == 2 and BlockColors[4] == 2 and BlockColors[8] == 2) :
        Label(master, text="Red Wins", bg="white").place(x = 1, y = 1, width=299, height=199)
        Label(master, text="", bg="white").place(x = 1, y = 200, width=299, height=100)
        Label(master, text="", bg="red").place(x = 101, y = 201, width=99, height=99)
        Button(master, text="Player 2 Wins", bg="red", fg="white").place(x = 101, y = 301, width=99, height=49)
        Finished3x3()
        print ("Red Wins")
    if (BlockColors[2] == 2 and BlockColors[4] == 2 and BlockColors[6] == 2) :
        Label(master, text="Red Wins", bg="white").place(x = 1, y = 1, width=299, height=199)
        Label(master, text="", bg="white").place(x = 1, y = 200, width=299, height=100)
        Label(master, text="", bg="red").place(x = 101, y = 201, width=99, height=99)
        Button(master, text="Player 2 Wins", bg="red", fg="white").place(x = 101, y = 301, width=99, height=49)
        Finished3x3()
        print ("Red Wins")    
    print(BlockColors)

def Restart() :
    print("New Game")
    global PlayedTurns
    global Player1Turn
    global Player2Turn
    global BlockColors
    PlayedTurns = 0
    Player1Turn = 1
    Player2Turn = 0
    BlockColors = [0,0,0,0,0,0,0,0,0]
    Label(master, text="", bg="black").place(x = 0, y = 0, width=300, height=350)
    Button(master, text="", bg="white", command=ButTop1).place(x = 1, y = 1, width=99, height=99)
    Button(master, text="", bg="white", command=ButTop2).place(x = 101, y = 1, width=99, height=99)
    Button(master, text="", bg="white", command=ButTop3).place(x = 201, y = 1, width=99, height=99)
    Button(master, text="", bg="white", command=ButMid1).place(x = 1, y = 101, width=99, height=99)
    Button(master, text="", bg="white", command=ButMid2).place(x = 101, y = 101, width=99, height=99)
    Button(master, text="", bg="white", command=ButMid3).place(x = 201, y = 101, width=99, height=99)
    Button(master, text="", bg="white", command=ButBot1).place(x = 1, y = 201, width=99, height=99)
    Button(master, text="", bg="white", command=ButBot2).place(x = 101, y = 201, width=99, height=99)
    Button(master, text="", bg="white", command=ButBot3).place(x = 201, y = 201, width=99, height=99)
    Button(master, text="Reset", bg="white", fg="red",command=Restart).place(x = 1, y = 301, width=99, height=49)
    Button(master, text="Player 1's Turn", bg="blue", fg="white").place(x = 101, y = 301, width=99, height=49)
    Button(master, text="Quit", bg="white", fg="red", command=master.destroy).place(x = 201, y = 301, width=99, height=49)

Restart()

mainloop()
