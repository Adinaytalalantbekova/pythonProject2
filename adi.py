
list1 = list()
list2 = []

list3 = (5, 2.5, 1, 2, 3, 4, 6)
odds = []
evens = []
for i in list3:
    if i % 2 == 0:
        evens.append(i)
    elif i % 2 !=0:
        odds.append(i)
print(sorted(odds))
print(sorted(evens))
#print(sorted(list3, reverse=True))



