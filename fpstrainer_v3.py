import tkinter as tk
import sys
import os
from tkinter.messagebox import askyesno
import random
import json
from tkinter import ttk

root = tk.Tk()
root.title("Simple FPS trainer")
root.geometry("500x500")
root.configure(bg="DarkOliveGreen4")
timer = 0
taskLists = ["w", "a", "s", "d", "space", "<Button>", "<Double-Button>", "<Triple-Button>"]
fileHighScore = "C:/Users/Gebruiker/Documents/ICT/file-remember/highscore.json"

def buttonTask():
    global taskLabel
    if timer > 0:
        task = random.choice(taskLists)
        taskLabel = tk.Label(root, text = "Press: " + task, font =("Arial", 14))
        taskLabel.pack()
        taskLabel.place(x=random.randint(0,385), y=random.randint(75,450))

        def keyTask(event):
            global points
            taskLabel.destroy()
            points += pointValue        
            labelPoints.configure(text = (str(points) + " points"))
            if task == "a" or task == "w" or task == "s" or task == "d" or task == "space":
                root.unbind("<"+task+">")
            root.after(500, buttonTask)

        if task == "<Button>" or task == "<Double-Button>" or task == "<Triple-Button>":
            pointValue = 2
            taskLabel.bind(task, keyTask)
            if task == "<Button>":
                taskLabel.configure(text = "Singel click")
            elif task == "<Double-Button>":
                taskLabel.configure(text = "Double click")
            elif task == "<Triple-Button>":
                taskLabel.configure(text = "Triple click")
        else:
            pointValue = 1
            root.bind(("<"+task+">"), keyTask)

def start():
    global timer, userName
    userName = name.get()
    infoLabel.destroy()
    startButton.destroy()
    nameEntry.destroy()
    labelTimer.configure(text ="Time remaining " + str(timer))
    if timer > 0:
        timer -= 1      
        root.after(1000, start)
    else:
        taskLabel.destroy()
        highscore(points)

def yesOrNo(): 
    answer = askyesno(
        title = "Again",
        message = "Congratulations, you have " + str(points) + " points, wanna play again?")
    if answer:
        frameScore.destroy()
        begin()
    else:
        root.destroy()

def showDictScore(dict):
    returnString = ""
    for v in dict.values():
        returnString += (str(v) + "\n")
    return returnString

def showDictName(dict):
    returnString = ""
    for k in dict.keys():
        returnString += (str(k) + ":\n")
    return returnString

def showDictNum():
    returnString = ""
    for i in range(1,11):
        returnString += str(i) + ".\n" 
    return returnString

def highscore(point):
    global frameScore
    with open(fileHighScore) as f:
        highScoreDict = json.load(f)
    
    def showScore():
        newHighScoreDict = {k: v for k, v in sorted(highScoreDict.items(), key=lambda item: item[1], reverse=True)}

        labelNum = ttk.Label(
            frameScore,
            text = showDictNum(),
            font = ("Arial", 16),
        )
        labelNum.grid(row = 0, column = 0)

        labelName = ttk.Label(
            frameScore,
            text = showDictName(newHighScoreDict),
            font = ("Arial", 16),
        )
        labelName.grid(row = 0, column = 1)

        labelScore = ttk.Label(
            frameScore,
            text = showDictScore(newHighScoreDict),
            font = ("Arial", 16)
        )
        labelScore.grid(row = 0, column = 2)

        doneButton = tk.Button(
            frameScore,
            font = ("Arial", 16),
            text = "Done",
            bg = "snow",
            fg = "grey5",
            command = yesOrNo
        )
        doneButton.grid(row = 1, column = 1)
        newScoreData = json.dumps(newHighScoreDict, indent = 1)
        os.remove(fileHighScore)
        with open(fileHighScore, "x") as x:
            x.writelines(newScoreData)

    frameScore = ttk.Frame(root)
    frameScore.place(relx = 0.5, rely = 0.5, anchor = "center")

    lastNum = list(highScoreDict.values())

    if point > lastNum[-1]:
        newHighScores = True
    else:
        newHighScores = False
            
    if newHighScores:
        highScoreDict.popitem()
        highScoreDict.update({userName: point})
        showScore()             
    else:
        showScore()
    

def begin():
    global timer, startButton, labelTimer, points, labelPoints, name, nameEntry, infoLabel
    timer = 20
    points = 0

    labelTimer = tk.Label(
        root,
        text = ("Time remaining " + str(timer)),
        font = ("Arial", 16),
        bg = "grey5",
        fg = "snow"
    )
    labelTimer.place(relwidth=0.5, anchor = "nw")

    labelPoints = tk.Label(
        root,
        text = (str(points) + " points"),
        font = ("Arial", 16),
        bg = "grey5",
        fg = "snow"
    )
    labelPoints.place(relx = 1.0,  relwidth=0.5, anchor = "ne")

    startButton = tk.Button(
        root,
        font = ("Arial", 16),
        bg = "snow",
        fg = "grey5",
        command = lambda:[start(), buttonTask()],
        text = "Start",
    )
    startButton.place(relx = 0.5, rely = 0.6, anchor = "center")
    
    name = tk.StringVar(value = "Player")
    nameEntry = tk.Entry(
        root,
        textvariable = name,
        font = ("Arial", 16),
        justify ="center"
    )
    nameEntry.place(relx = 0.5, rely = 0.5, anchor = "center")

    infoLabel = tk.Label(
        root,
        text = "Write your name\nand then press the start button",
        font = ("Arial", 16),
        bg = "DarkOliveGreen4",
    )
    infoLabel.place(relx = 0.5, rely = 0.4, anchor = "center")

begin()

root.mainloop()