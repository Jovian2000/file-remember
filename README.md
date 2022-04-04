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
    if os.path.exists("C:/Users/Gebruiker/OneDrive/Bureaublad/ICT/file-remember/data/" + titleData):
        num += 1
        titleData = "datanaamlijst" + str(num)
    else:
        folderData = open("C:/Users/Gebruiker/OneDrive/Bureaublad/ICT/file-remember/data/" + titleData,"x")
        folderData.writelines(namesData)
        break
```
### aanpassing
ik heb de namen met een timestamp gedaan waardoor hij niet hoeft te controleren op dubbele namen en het word nu ook opgeslagen als een json file
``` python
titleData = "data_naamlijst_(" + str(datetime.datetime.now().timestamp()) + ").json"
with open("C:/Users/Gebruiker/OneDrive/Bureaublad/ICT/file-remember/data/" + titleData,"x") as f:
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
