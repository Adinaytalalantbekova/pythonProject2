#Словари и множество

names = ('one', 'two', 'three', 'four')
numbers = 1, 2, 3, 4


#for i in range(1, 5):
 #   numbers.append(i)

dict_3 = dict(zip(numbers, names))

if '3' in dict_3:
    print(dict_3[3])

#print(numbers)
#print(dict_3)

dict_4 = dict([(2, 'djhgf'),(9, 'dg'),(names, 'three'),(numbers, 'dhfjg')])
#print(dict_4)


#dict_1 = {
  #  'def': 1,
 #   'if': 2,
#   'three': 3,
 #   'four': 4,
  #  'numbers': [1, 2, 3],
 #   'names': names,
#}

#print(dict_1['names'])


#student = dict(name='Azat', age='19')

#print(student)
#print(dict_2)

#del dict_1['names']
#dict_1.pop('numbers')

#print(dict_1)

#dict_1['five'] = 5
#print(dict_1)

#dict_1['def'] = 'definition'
#dict_1['if'] = 'condition'
#print(student)
#print(dict_1)

#ct_1.update(student)
a = {**dict_3, **dict_4}
print(a)
#print(dict_1)

#for value in dict_1.items():
 #   print(value)

#for key in dict_1.items():
#    print(key)

#for key, value in dict_1.items():
#    print(key, 'это', value)



