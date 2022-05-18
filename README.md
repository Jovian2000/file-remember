# file-remember
## F1.09.03.O2 - Wie had wie ook alweer?
Heb mijn naamlootjes aangepast, met deze code maakt hij steeds nieuwe bestanden aan voor welke persoon wie heeft getrokken.
Hij controleert ook of de naam van de bestand al bestaat en als dat zo is dan maakt hij een nieuwe naam voor
``` python
import json
import os.path

namesData = json.dumps(namesDict, indent = 2)
dictionaryData = json.loads(namesData)

num = 1
titleData = "datanaamlijst" + str(num)

while True:
    if os.path.exists("C:/Users/Gebruiker/Documents/ICT/file-remember/data/" + titleData):
        num += 1
        titleData = "datanaamlijst" + str(num)
    else:
        folderData = open("C:/Users/Gebruiker/Documents/ICT/file-remember/data/" + titleData,"x")
        folderData.writelines(namesData)
        break
```
### aanpassing
ik heb de namen met een timestamp gedaan waardoor hij niet hoeft te controleren op dubbele namen en het word nu ook opgeslagen als een json file
``` python
titleData = "data_naamlijst_(" + str(datetime.datetime.now().timestamp()) + ").json"
with open("C:/Users/Gebruiker/Documents/ICT/file-remember/data/" + titleData,"x") as f:
    f.writelines(namesData)
```
## F1.09.03.O3 - Continue from autosave?
Ik had de hele game die ik eerder had moeten maken helemaal aangepast, maar nu heeft het ook een autosave.
Dit zijn de belangrijkste voor de auto save
``` python

fileName = "C:/Users/Gebruiker/Documents/ICT/file-remember/autosave.json"
num = 0

if os.path.exists(fileName):    
    askContinue = input("Do you want to continue from last save? (Y/N)\n")
    if askContinue == "y" or askContinue == "Y":
        with open(fileName, "r") as n:
            num = int(n.read())
    os.remove(fileName)

for i in range(num, len(listStage)):
    with open(fileName, "x") as j:
        j.write(str(i))
    if game(listStage[i], listStory[i], listQuestions[i], listAnswer[i], listFailure[i]) == False:
        lose()
        break
    os.remove(fileName)
```
### aanpassingen
Dit zijn de volgende aanpassingen. Ik heb het nu echt een dictionary van wat het programma moet opslaan gemaakt waardoor het meer op een json format lijkt.
Het onthoud nu ook de naam die je hebt ingevoerd.
``` python
if os.path.exists(fileName):    
    with open(fileName, "r") as n:
        loadedData = json.load(n)
        if type(loadedData["Stage"]) == int:
            askContinue = input("Do you want to continue from last save? (Y/N)\n").lower()
            if askContinue == "y":
                for k, v in loadedData.items():
                    num = loadedData["Stage"]
                    name = loadedData["Name"]
            else:
                name = input("Name: ")
        else:
            name = input("Name: ")
    os.remove(fileName)
else:
    name = input("Name: ")
```
``` python
for i in range(num, len(listStage)):
    gameDict = {"Name" : name,"Stage" : i}
    gameData = json.dumps(gameDict, indent=1)
    with open(fileName, "x") as j:
        j.writelines(gameData)
    if game(listStage[i], listStory[i], listQuestions[i], listAnswer[i], listFailure[i]) == False:
        lose()
        break
    os.remove(fileName)
<<<<<<< HEAD
```
## F1.09.03.O4 - FPS trainer Highscores
FPS trainer V1 is aangepast met een highscore, dit is de belangrijkste functie die erbij is toegevoegd
``` python

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
=======
>>>>>>> 0bc11f6bdf53246d98f8ee353b6171b15cb9db3b
```