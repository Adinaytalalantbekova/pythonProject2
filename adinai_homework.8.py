from random import randint
import datetime

row = int(input("Сколько попыток? "))
row1 = row
name = input("Укажите имя: ")
start = datetime.datetime.now()

while 1:
    comp = randint(1, 9)
    comp1 = randint(1, 9)
    row1 -= 1
    print(comp, '*', comp1, end=' = ')
    a = int(input())
    m = comp * comp1
    print(m)
    with open('result.txt', 'a') as res:
        if m == a:
            res.write(f"{comp} * {comp1} = {a} ({m}) правильно\n")
        if m != a:
            res.write(f"{comp} * {comp1} = {a} ({m}) неправильно\n")
    if row1 == 0:
        end = datetime.datetime.now()
        with open('result.txt', 'a') as res:
            res.write(f'Попытки: {row}, '
                      f'имя: {name}'
                      f', время: {end - start}\n')

        break
