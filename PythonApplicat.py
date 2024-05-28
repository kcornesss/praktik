from turtle import *

# sozdanie pola
def drawField(a):
    t = Turtle()
    t.speed(0)
    t.hideturtle()
    for j in range(3):
        t.up()
        t.color("black")
        t.goto(0, -a * j)
        for i in range(3):
            t.down()
            for n in range(4):
                t.fd(a)
                t.left(90)
            t.up()
            t.fd(a)
            xCenters.append(t.position()[0] - a / 2)
            yCenters.append(t.position()[1] + a / 2)
            
checkList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# sozdanie krestika
def drawCross(a, recNum):
    t = Turtle()
    t.speed(0)
    t.hideturtle()
    crosses.append(recNum)
    t.up()
    t.color("red")
    t.goto(xCenters[recNum - 1], yCenters[recNum - 1])
    t.down()
    t.left(45)
    for i in range(4):
        t.fd(a / 2)
        t.backward(a / 2)
        t.left(90)
    checkList.remove(recNum)

#sozdanie nolika 
def drawCircle(a, recNum):
    t = Turtle()
    t.speed(0)
    t.hideturtle()
    circles.append(recNum)
    t.color("green")
    t.up()
    t.goto(xCenters[recNum - 1], yCenters[recNum - 1] - r)
    t.down()
    t.circle(r)
    checkList.remove(recNum)

#sozdanie peremennih
xCenters = []
yCenters = []
crosses = []
circles = []
a = 50
r = 20

#risyem pole
drawField(a)

#proverka viigrashnih kombinaciié
def lineCheck(figure):
    if figure == "crosses":
        return any(
            listInListCheck(combination, crosses)
            for combination in winning_combinations
        )
    else:
        return any(
            listInListCheck(combination, circles)
            for combination in winning_combinations
        )

winning_combinations = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9], 
    [1, 4, 7], [2, 5, 8], [3, 6, 9], 
    [1, 5, 9], [3, 5, 7]
]

#proverka kakaya figyra kakomy kvadraty sootvetstvyet
def listInListCheck(list1, list2):
    return all(element in list2 for element in list1)

#sozdanie peremennih dla vihoda iz cikla
turns = 0
isLine = False

while turns < 9 and not isLine:
    #hod krestikov
    recNum = int(input("Where do we put the cross? (squares from 1 to 9 from left to right)? "))
    isCorrect = False
    #proverka vernosti vvedonnih dannih
    while not isCorrect:
        if recNum in checkList and 1 <= recNum <= 9:
            isCorrect = True
        elif recNum < 1 or recNum > 9:
            recNum = int(input("There is no such square, enter another: "))
        elif recNum not in checkList:
            recNum = int(input("There is already something in this square, enter another: "))
    #risyem krestik i proveraem na viigrish 
    drawCross(a, recNum)
    isLine = lineCheck("crosses")
    if isLine == True:
        print("The crosses have won!")
        break
    turns += 1
    if turns == 9:
        continue
    
    #hod nolikov
    recNum = int(input("Where do we put the zero? (squares from 1 to 9 from left to right)? "))
    isCorrect = False
    #proverka vernosti vvedonnih dannih
    while not isCorrect:
        if recNum in checkList and 1 <= recNum <= 9:
            isCorrect = True
        elif recNum < 1 or recNum > 9:
            recNum = int(input("There is no such square, enter another: "))
        elif recNum not in checkList:
            recNum = int(input("There is already something in this square, enter another: "))
    #risyem nolik i proveraem na viigrish
    drawCircle(a, recNum)
    isLine = lineCheck("circles")
    if isLine:
        input("The zeroes have won!")
        break
    turns += 1
#slychai nichei
if turns == 9:
    print("Draw!")
from turtle import *

# sozdanie pola
def drawField(a):
    t = Turtle()
    t.speed(0)
    t.hideturtle()
    for j in range(3):
        t.up()
        t.color("black")
        t.goto(0, -a * j)
        for i in range(3):
            t.down()
            for n in range(4):
                t.fd(a)
                t.left(90)
            t.up()
            t.fd(a)
            xCenters.append(t.position()[0] - a / 2)
            yCenters.append(t.position()[1] + a / 2)
            
checkList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# sozdanie krestika
def drawCross(a, recNum):
    t = Turtle()
    t.speed(0)
    t.hideturtle()
    crosses.append(recNum)
    t.up()
    t.color("red")
    t.goto(xCenters[recNum - 1], yCenters[recNum - 1])
    t.down()
    t.left(45)
    for i in range(4):
        t.fd(a / 2)
        t.backward(a / 2)
        t.left(90)
    checkList.remove(recNum)

#sozdanie nolika 
def drawCircle(a, recNum):
    t = Turtle()
    t.speed(0)
    t.hideturtle()
    circles.append(recNum)
    t.color("green")
    t.up()
    t.goto(xCenters[recNum - 1], yCenters[recNum - 1] - r)
    t.down()
    t.circle(r)
    checkList.remove(recNum)

#sozdanie peremennih
xCenters = []
yCenters = []
crosses = []
circles = []
a = 50
r = 20

#risyem pole
drawField(a)

#proverka viigrashnih kombinaciié
def lineCheck(figure):
    if figure == "crosses":
        return any(
            listInListCheck(combination, crosses)
            for combination in winning_combinations
        )
    else:
        return any(
            listInListCheck(combination, circles)
            for combination in winning_combinations
        )

winning_combinations = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9], 
    [1, 4, 7], [2, 5, 8], [3, 6, 9], 
    [1, 5, 9], [3, 5, 7]
]

#proverka kakaya figyra kakomy kvadraty sootvetstvyet
def listInListCheck(list1, list2):
    return all(element in list2 for element in list1)

#sozdanie peremennih dla vihoda iz cikla
turns = 0
isLine = False

while turns < 9 and not isLine:
    #hod krestikov
    recNum = int(input("Where do we put the cross? (squares from 1 to 9 from left to right)? "))
    isCorrect = False
    #proverka vernosti vvedonnih dannih
    while not isCorrect:
        if recNum in checkList and 1 <= recNum <= 9:
            isCorrect = True
        elif recNum < 1 or recNum > 9: 
            recNum = int(input("There is no such square, enter another: "))
        elif recNum not in checkList:
            recNum = int(input("There is already something in this square, enter another: "))
    #risyem krestik i proveraem na viigrish 
    drawCross(a, recNum)
    isLine = lineCheck("crosses")
    if isLine == True:
        print("The crosses have won!")
        break
    turns += 1
    if turns == 9:
        continue
    
    #hod nolikov
    recNum = int(input("Where do we put the zero? (squares from 1 to 9 from left to right)? "))
    isCorrect = False
    #proverka vernosti vvedonnih dannih
    while not isCorrect:
        if recNum in checkList and 1 <= recNum <= 9:
            isCorrect = True
        elif recNum < 1 or recNum > 9:
            recNum = int(input("There is no such square, enter another: "))
        elif recNum not in checkList:
            recNum = int(input("There is already something in this square, enter another: "))
    #risyem nolik i proveraem na viigrish
    drawCircle(a, recNum)
    isLine = lineCheck("circles")
    if isLine:
        input("The zeroes have won!")
        break
    turns += 1
#slychai nichei
if turns == 9:
    print("Draw!")

