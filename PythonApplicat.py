from turtle import *
def drawField(a):
    t = Turtle()
    t.speed(0)
    t.hideturtle()
    for j in range(3):
        t.up()
        t.color("black")
        t.goto(0,-a*j)
        for i in range(3):
            t.down()
            for n in range(4):
                t.fd(a)
                t.left(90)
            t.up()
            t.fd(a)
            xCenters.append(t.position()[0] - a/2)
            yCenters.append(t.position()[1] + a/2)   
            
def drawCross(a, recNum):
    t = Turtle()
    t.speed(0)
    t.hideturtle()
    crosses.append(recNum)
    t.up()
    t.color("red")
    t.goto(xCenters[recNum-1],yCenters[recNum-1])
    t.down()
    t.left(45)
    for i in range(4):
        t.fd(a/2)
        t.backward(a/2)
        t.left(90)
    checkList.remove(recNum)
    
def drawCircle(a, recNum):
    t = Turtle()
    t.speed(0)
    t.hideturtle()
    circles.append(recNum)
    t.color("green")
    t.up()
    t.goto(xCenters[recNum-1] ,yCenters[recNum-1] - r)
    t.down()
    t.circle(r)
    checkList.remove(recNum)

xCenters = []
yCenters = []
crosses = []
circles = []
a = 50
r = 20
drawField(a)
checkList = [1,2,3,4,5,6,7,8,9]

def lineCheck(figure):
    if figure == "��������":
        if listInListCheck([1,2,3], crosses) or listInListCheck([4,5,6], crosses) or listInListCheck([7,8,9], crosses) \
        or listInListCheck([1,4,7], crosses) or listInListCheck([2,5,8], crosses) or listInListCheck([3,6,9], crosses)\
        or listInListCheck([1,5,9], crosses) or listInListCheck([3,5,7], crosses):
            return True
    else:
        if listInListCheck([1,2,3], circles) or listInListCheck([4,5,6], circles) or listInListCheck([7,8,9], circles) \
        or listInListCheck([1,4,7], circles) or listInListCheck([2,5,8], circles) or listInListCheck([3,6,9], circles) \
        or listInListCheck([1,5,9], circles) or listInListCheck([3,5,7], circles):
            return True
    return False

def listInListCheck(list1,list2):
    for element in list1:
        if element not in list2:
            return False
    return True

turns = 0
isLine = False
while turns < 9 and not isLine:
    recNum = int(input("���� ������ �������?"))
    isCorrect = False
    while not isCorrect:
        if recNum in checkList and recNum <= 9:
            isCorrect = True;
        elif recNum > 9 or recNum < 1:
            recNum = int(input("���, ������ �������� ���, ������� ������:"))
        elif recNum not in checkList:
            recNum = int(input("� ������ �������� ��� ���-�� ����, ������� ������:"))
    drawCross(30,recNum)
    isLine = lineCheck("��������")
    if isLine:
        input("�������� ��������!")
        break
    turns += 1;
    if turns == 9:
        continue
    
    recNum = int(input("���� ������ �����?"))
    isCorrect = False
    while not isCorrect:
        if recNum in checkList and recNum <= 9:
            isCorrect = True
        elif recNum > 9 or recNum < 1:
            recNum = int(input("���, ������ �������� ���, ������� ������:"))
        elif recNum not in checkList:
            recNum = int(input("� ������ �������� ��� ���-�� ����, ������� ������:"))
    drawCircle(15,recNum)
    isLine = lineCheck("������")
    if isLine:
        input("������ ��������!")
        break
    turns += 1;
if turns == 9:
    print("�����!")
