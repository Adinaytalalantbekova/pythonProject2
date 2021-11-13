# from pprint import pprint
#
# with open('result.txt', 'w') as file:
#     file.write(' My name is adinai \n')
#
# with open('result.txt', 'a') as file:
#     file.write('I am from USA \n')
#
# with open('result.txt', 'r') as file:
#     pprint(file.read())



# import time
#
# with open('result.txt') as gpm:
#     for line in gpm:
#         for i in line:
#             print(i, end='')
#             time.sleep(0.1)

# игра в кости

from random import randint
from datetime import datetime


attempts = int(input("введиде количество попыток: "))
cash = 100
while attempts != 0:
    player = [randint(1, 6), randint(1, 6)]
    comp = [randint(1, 6), randint(1, 6)]

    bet = int(input(f"Cделайте ставку: ,Доступно:{cash}"))

    if bet < 1 or bet > cash:
        print("Cтавка не должно превышать сумму")
        continue
    attempts -= 1
    if sum(player) > sum(comp):

        cash += bet
    elif sum(player) < sum(comp):
        cash += bet
    else:
        pass
    print(cash)

    print('Player:', player,)
    print("Comp", comp)



