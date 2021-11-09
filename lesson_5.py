# def plus(a, b):
#     return a + b
# result = plus(5, 10)
# print(plus(2, plus(result)))
# from lesson_4_1 import menu
#
#
# def schedule(drink, lunch, dissert):
#     return {'напиток': drink, 'обед': lunch, 'десерт':dissert}
# def show(dict1):
#     for i, k in dict1.items():
#          print(i,"-", k)
#
# monday = menu("компот", "суп", "брауини")
# tuesday = menu(dissert="пирожное", drink="сок", lunch="омлет")
# friday = menu('чай', 'борщ')
# print(monday)
# print(tuesday)
# print(friday)
#
# show(monday)
# show(menu(dessert="пирожное", drink="сок", lunch="омлент"))
def plus(a, *args):
    return sum(args)

print(plus(4,4,4,4))

def dct(**kwargs):
    print(kwargs)

dct(a=1, b=2, c=3)
