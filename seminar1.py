
import math

def task1():

    # За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров? При решении этой задачи нельзя
    # пользоваться условной инструкцией if и циклами.

    n = int(input("Введите количество км, которая проезжает машина за один день: "))

    m = int(input("Введите расстояние, которое нужно проехать: "))

    v = int(n/24)

    t = int(m/v)

    day = math.ceil(t/24)

    print(f"расстояние {m} км со скоростью {v}км/ч машина проедет за {day} дней")

def task2():

    # Найдите сумму цифр трехзначного числа.    

    n = int(input("Введите целое число: "))

    m = n

    sumDigitNumber = 0

    while (n > 0):

        sumDigitNumber += n % 10

        n =int( n / 10)

    print(f"Сумма цифр вашего числа {m} = {sumDigitNumber}")    
    


import math

def task3():

    # В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами. За каждой партой
    # может сидеть два учащихся. Известно количество учащихся в каждом из трех классов. Выведите наименьшее число парт,
    # которое нужно приобрести для них.

    print("Введите количечтво учащихся в классе №1: ")

    x = int(input())

    print("Введите количечтво учащихся в классе №2: ")

    y = int(input())

    print("Введите количечтво учащихся в классе №3: ")

    z = int(input())

    sumStudent = int(x + y + z)

    needTables = math.ceil(sumStudent / 2)

    print(f"необходимо парт для всех этих школьников минимум {needTables}")

def task4():

    #      Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый
    # ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов,
    # чем Петя и Сережа вместе?

    s = int(input("Введите четное число количество журавликов, которые сделали Петя, Катя и Сережа вместе: "))

    petya =int( s / 3 / 2)

    sereja = petya

    katya = int((petya + sereja) * 2)
    
    print(f" Всего сделали = {s} \n Петя сделал - {petya}\n Сережа сделал - {sereja}\n Катя сделала - {katya} ")





def task5():

#     Вагоны в электричке пронумерованы натуральными числами, начиная с 1 (при этом иногда вагоны нумеруются от «головы» поезда, а иногда – с
# «хвоста»; это зависит от того, в какую сторону едет электричка). В каждом вагоне написан его номер.Витя сел в i-й вагон от головы поезда 
# и обнаружил, что его вагон имеет номер j. Он хочет определить, сколько всего вагонов в электричке. Напишите программу, которая будет
# это делать или сообщать, что без дополнительной информации это сделать невозможно.


    i = int(input("Введите номер вашего вагона при посадке: "))

    j = int(input("Введите номер вашего вагона по прибытию: "))
    
    sumStartToEnd = 0

    for k in range(1,i+1,1):

        sumStartToEnd+=1

    sumEndToStart = 0

    for k in range(1,j+1,1):

        sumEndToStart+=1

    sumRailwayCarriage = sumStartToEnd + sumEndToStart  - 1

    print(f"Количество вагонов в поезде состовляет  {sumRailwayCarriage} ед.")  



def task7():

    # Дано натуральное число. Требуется определить, является ли год с данным номером високосным. Если год является високосным, то выведите YES,
    # иначе выведите NO. Напомним, что в соответствии с григорианским календарем, год является високосным, если его номер кратен 4, 
    # но не кратен 100, а также если он кратен 400.

    year = int(input("Введите четырехзначное целое число, которое будет обозначать номер года: "))

    if(year % 400 == 0 or year % 100 != 0 and year % 4 == 0): print( f" {year} год весокосный - YES")

    else : print(f" {year} год весокосный - NO")




task = int(input("Введите номер задачи 1, 3, 5 или 7: "))

if (task ==1) : task1()

elif (task == 2) : task2()

elif(task == 3): task3()

elif(task == 4): task4()

elif(task == 5) : task5()

elif(task == 7) : task7()

else:print("задачи с таким номером не существует!") 




    
