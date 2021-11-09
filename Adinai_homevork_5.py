# a)
def multiplication(ab, cd):
    return(float(ab * cd))
multiplication(3.5, 4.7)
# b)
def arif(*args):
    summa = 0
    for i in args:
        summa += i
    return int(summa/len(args))
print(arif(1,2,3,4,5,6,7,8,9))
# c)
def menu(breakfast,lunch,diner):
    return {'завтрак': breakfast, 'обед': lunch, 'ужин': diner}
def show(dict1: dict):
    for i, p in dict1.items():
        print(i,"-", p)
monday = menu('чай c випичком', 'суп','манты')
print(monday)
show(monday)