import os.path, json, os

def lose():
    global win
    win = False
    print("Game over!")

def game(stage, story, questions, answer, failure):
    print("\nStage: " + str(stage) + "\n")
    print(story + "\n")
    print(questions + "\n")
    userAnswer = input(name + ": ").lower()
    print(name + " choose " + userAnswer)
    if userAnswer == answer:
        return True
    else:
        print(failure)
        return False

fileName = "C:/Users/Gebruiker/Documents/ICT/file-remember/autosave.json"

print("---------------------------------------------")
print("         Welcome                             ")
print("You will enter a cave to steal               ")
print("a precious gem, but be carefull!             ")
print("This cave is extremely dangerous,            ")
print("one wrong way and you die!                   ")
print("---------------------------------------------")
print("Rules:\nType correctly or you wil automatically\nchoose the wrong path\n")

num = 0
win = True
listStage = []
listStory = []
listQuestions = []
listAnswer = ["b", "d", "a", "a", "c", "416", "5", "a", "4165", "b"]
listFailure = []

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

for x in range(1,11):
    listStage.append(x)

listStory.append("You find your self in the entrance of the dangerous cave. You enter the cave and you see 2 paths.\nThey both have signs.\nThe left one says this way for the gem an the right one says no entry.\n")
listQuestions.append("Which way are you choosing?\nA: Left\nB: Right")
listFailure.append(name + " enters the left path and suddenly a giant rock falls from above.\nIt was impossible to dodge the giant rock.\nIt appears the sign was a trap for anyone who tries to steal the gem." )

listStory.append("Good job, obviously it would be a trap if you chose the obvious path.\n" + name + " enters the right path and sees a room and at the end of the room a closed door.\nThere is a bucket with unlimited stones, an empty vase in the middle of the room\nand on the wall you see a sign that says:\n'Put the right ammount in the vase and the door will open.'\n" + name + " also sees: 'hint: 5 x 3 - 2 x 5 + 3'")
listQuestions.append("How many stones do you put in the vase?\nA: 3\nB: 4\nC: 6\nD: 8")
listFailure.append("Thats not enough!\nThe ground opens up and " + name + " falls in a sea of lava")

listStory.append("After " + name + " puts stones in the vase, the closed door slowly turns open.\n" + name + " walks through the door and sees another room with an iron shield, a sword\nand a bow and arrow. " + name + " picks up the weapons and walks further. Suddenly a giant\ndragon appears. "  + name + " took out his weapons and decided to take on the giant dragon.")
listQuestions.append("What is your first move?\nA: Use your shield to charge forward and use the sword to strike the dragon\nB: Use your bow and arrow to hit the dragon")
listFailure.append("After trying to shoot, the dragon spit fire and burns " + name + ".")

listStory.append("After a succesfull hit, the dragon screamed and was ready to attack\nfrom above. " + name + " use his shield to block some attacks and\ntries to dodge the heavy attacks. Now its time to use his bow.")
listQuestions.append("How many arrows will you shoot?\nA: 4\nB: 6\nC: 8\nD: 10")
listFailure.append(name + " shoots his arrows, but the dragon attacks and " + name + " was\ntoo focused with his shots. Because " + name + " tries to shoot so many,\nthe dragon managed to hit him hard and " + name + " died.")

listStory.append("After shooting the arrows, the dragon goes for another attack.\n" + name + " managed to dodge because he didn't try to shoot too much.\nThe dragon landed back on the ground. It looks like he needs to rest\nafter the shots. Now is your chance to strike.")
listQuestions.append("How many strikes will you use with your sword?\nA: 1\nB: 4\nC: 6\nD: 5")
listFailure.append("Thats not enough! The dragon wakes up and bites " + name + " lower half.\n" + name + " can't do anything, bleeds out and dies.")

listStory.append("Thats enough strikes, the dragon dies and " + name + " walks further.\nThere is another room with 1 question, it looks like you have to answer\nit correctly or else something bad will happen.")
listQuestions.append("What is 32x13?")
listFailure.append("Thats the wrong answer. Suddenly the room gets filled with lava and\n" + name + " can't see a way out and dies.")

listStory.append("Thats the correct answers. The next door opens up and " + name + " enters the\nnext room. There is another vase and a sign that says: 'Pentagon\n" + name + " sees another bucket of stones and tries to fill the vase")
listQuestions.append("How many stones this time?")
listFailure.append("Thats the wrong answer. Pentagon means something with 5\nThe room starts to collapse and " + name + " dies!")

listStory.append("Good job! Pentagon means something with 5.\nThe next door opens and " + name + " sees a room with 2 paths again.\nThis time there is only 1 sign that says:'Only 1 way correct'.")
listQuestions.append("Which way are you going?\nA: Left\nB: Right")
listFailure.append("Thats the wrong path." + name + " gets attacked by poisoned bats\n" + name + " dies because of the poison")

listStory.append("It looks like this is the good path, nothing bad happened\n" + name + " sees another closed door. There is a lock and you need\nto put the right code to open it.")
listQuestions.append("What is the code? (hint: the numbers you saw earlier in the game)")
listFailure.append("Thats the wrong code!\nThe room explodes instantly and " + name + " dies!")

listStory.append("Nice! It looks like thats the right code. The door opens.\nAnother room with a stone guard in front of the last door.\nThe guard says: 'Intruder!'. The stone guard attacks, but\nluckily you have your weapons.")
listQuestions.append("What is your next move?\nA: Use sword to strike the guard\nB: Use shield to charge\nC: Use bow and arrow to shoot")
listFailure.append("The weapon you chose didn't work.\nThe guard hit " + name + " with a hammer and " + name + " dies.")

winText = name + " charged the guard and the guard instantly breaks into pieces.\nAfter the guard dies, " + name + " sees the open door that was behind\nthe guard. " + name + " entered the last room and sees the gem.\n" + name + " picks up the gem and leaves the dangerous cave.\n\nThe end!\n\nCongratulations!!!!"

for i in range(num, len(listStage)):
    gameDict = {"Name" : name,"Stage" : i}
    gameData = json.dumps(gameDict, indent=1)
    with open(fileName, "x") as j:
        j.writelines(gameData)
    if game(listStage[i], listStory[i], listQuestions[i], listAnswer[i], listFailure[i]) == False:
        lose()
        break
    os.remove(fileName)
    
if win:
    print(winText)
