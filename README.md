# file-remember
## F1.09.03.O2 - Wie had wie ook alweer?
Heb mijn naamlootjes aangepast, met deze code maakt hij steeds nieuwe bestanden aan voor welke persoon wie heeft getrokken.
Hij controleert ook of de naam van de bestand al bestaat en als dat zo is dan maakt hij een nieuwe naam voor
``` python
import json
import os.path

namesData = json.dumps(namesDict)
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