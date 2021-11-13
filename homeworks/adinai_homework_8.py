from random import randint
import datetime

row = int(input("Сколько попыток? "))
row1 = row
name = input("Укажите имя: ")
start = datetime.datetime.now()
#
    while 1:
        comp = randint(1, 9)
        comp1 = randint(1, 9)
        row1 -= 1
        print(comp, '*', comp1, end=' = ')
        a = int(input())
        m = comp * comp1
        print(m)
        with open("../result.txt", "a") as res:
            if m == a:
                res.write(f"{comp} * {comp1} = {a} ({m}) правилбно \n")
            if m != a:
                res.write(f"{comp} * {comp1} = {a} ({m}) правилбно \n")
                      f'{comp} * {comp1} = {m}\n'
                      f"{start.strftime('%X')}\n"
                      f"{datetime.datetime.now().strftime('%X')}\n")
            break


