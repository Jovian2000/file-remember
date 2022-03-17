import random
import json
import os.path
import datetime 
names = []
namesDict = {}
lottery = []
namesPulled = []
nameLimit = 2
a = ""

print("\nLootjes generator. Voer de namen in. \n(stop = hele programma stoppen)")
print("Namen:")

while True:
    names.append(input(""))
    if "stop" in names:
        names.clear()
        break
    if len(names) > nameLimit:
        if "klaar" in names:
            break
        print("U heeft genoeg namen. Als u de lootjes wilt trekken, typ 'klaar'.")
    else: 
        print("U moet nog " + str(nameLimit - len(names) + 1) + " namen invoeren") 
names.remove("klaar")

names = list(dict.fromkeys(names))
lottery.extend(names)

def pullingNames():
    global lottery, namesPulled, a
    a = random.choice(lottery)
    namesPulled.append(a)
    lottery.remove(a)

for x in range(len(names)):
    if names[x] in lottery: 
        lottery.remove(names[x])
        pullingNames()
        lottery.append(names[x])
    else:    
        pullingNames()

for i in range(len(names)):    
    namesDict.update({names[i]: namesPulled[i]})
print("")
for m, n in namesDict.items():
    print(m + ": " + n)

namesData = json.dumps(namesDict, indent = 2)
dictionaryData = json.loads(namesData)

# num = 1

# titleData = "datanaamlijst" + str(num)

# while True:
#     if os.path.exists("C:/Users/Gebruiker/OneDrive/Bureaublad/ICT/file-remember/data/" + titleData):
#         num += 1
#         titleData = "datanaamlijst" + str(num)
#     else:
#         folderData = open("C:/Users/Gebruiker/OneDrive/Bureaublad/ICT/file-remember/data/" + titleData,"x")
#         folderData.writelines(namesData)
#         break

titleData = "data_naamlijst_(" + str(datetime.datetime.now().timestamp()) + ")"
with open("C:/Users/Gebruiker/OneDrive/Bureaublad/ICT/file-remember/data/" + titleData,"x") as f:
    f.writelines(namesData)
