Крестики-нолики на Python

Креестики-нолики — логическая игра между двумя противниками на квадратном поле 3 на 3 клетки. Один из игроков играет «крестиками», второй — «ноликами».

Правила игры
Игроки по очереди ставят на свободные клетки поля 3×3 знаки (один всегда крестики, другой всегда нолики). Первый, выстроивший в ряд 3 своих фигуры по вертикали, горизонтали или большой диагонали, выигрывает. Если игроки заполнили все 9 ячеек и оказалось, что ни в одной вертикали, горизонтали или большой диагонали нет трёх одинаковых знаков, партия считается закончившейся в ничью. Первый ход делает игрок, ставящий крестики.
Обычно по завершении партии выигравшая сторона зачёркивает чертой свои три знака (нолика или крестика), составляющих сплошной ряд.

Видео-демонстрация https://disk.yandex.ru/i/MvMuFLkzXmNBHQ

Игра реализована, как консольная, поэтому для её запуска необходимы только установленный язык программирования Python и файл с программой.

Программа в большинстве своём реализована библиотекой turtle, использованы говорящие названия, так что, любой знакомый с этой библиотекой и языком с лёгкостью может разобраться в коде.

Названия и назначения переменных:
t - сокращение названия и вызова библиотеки Turtle().
xCenters - список координат x введённых фигур.
yCenters - список координат y введённых фигур.
crosses - список квадратов, занятых крестиками.
circles - список квадратов, занятых ноликами.
a - длина/ширина квадрата.
r - радиус круга (нолика).
checkList - список доступных для заполнения квадратов.
turns - количество сделаных ходов.
isLine - "флаг" для оствновки основного цикла.
recNum - введённый квадрат
isCorrect - "флаг" для проверки верности введённых данных.

Назначения функций:
def drawField(a) - "рисует" поле для крестиков-ноликов, где каждая клетка шириной в а пикселей.
def drawCross(a, recNum) - "рисует" крестик в введённом в recNum квадрате.
def drawCircle(a, recNum) - "рисует" нолик в введённом в recNum квадрате.
def lineCheck(figure) - проверяет не заполнена ли какая-либо вертикаль/горизонталь/диагональ одинаковыми фигурами.
def listInListCheck(list1,list2) - проверяет содержат ли ряды крестиков или ноликов комбинации выигрышных ходов в игре крестики-нолики.


Взаимодействие с пользователем
В консоли поочерёдно спрашивается, куда ввести крестик и нолик. На вход принимаются числа от 1 до 9, квадраты считаюся слева-направо. При вводе числа, не входящего в данный диапозон или до этого введённого числа, программа об этом сообщает и переспрашивает. Введение иных символов не предусмотрено. При заполнении какой-либо вертикали/горизонтали/диагонали одинаковыми фигурами или заполнении всех квадратов, программа сообщает о победе одной из сторон или ничьей соответственно.

Блок-схемы:
"main"
![image](https://github.com/kcornesss/praktik/assets/116918339/774e6f93-6b3e-4221-9015-fc01234567ae)

drawField
![image](https://github.com/kcornesss/praktik/assets/116918339/c2978bcc-bdb9-481b-87ed-59b84281d5b0)

drawCross
![image](https://github.com/kcornesss/praktik/assets/116918339/0835fa57-172b-4dd5-a1f2-40a3e921a5e1)

drawCircle
![image](https://github.com/kcornesss/praktik/assets/116918339/f0c6495f-a8ea-4557-a2d4-8965887ef6cb)

lineCheck
![image](https://github.com/kcornesss/praktik/assets/116918339/19106bd6-1951-4910-94f8-9a2d76c9265f)

listInListCheck
![image](https://github.com/kcornesss/praktik/assets/116918339/32071eb0-16cc-486e-90e4-60822fdd1a47)




