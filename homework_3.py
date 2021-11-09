letters = []
numbers = []

data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'K', 'e',  3, 'e', 1, 'G')
for element in data_tuple:
    if(type(element)==str):
        letters.append(element)
    else:
        numbers.append(element)
print(letters)
print(numbers)
numbers.remove(6.13)
true = numbers.pop(0)
letters.append(true)
print(letters)
print(numbers)
numbers.insert(1, 2)
print(numbers)
numbers = sorted(numbers)
print(numbers)
letters.reverse()
print(letters)
letters[4] = 'k'
letters[7] = 'c'
print(letters)
numbers = tuple(numbers)
letters = tuple(letters)
print(letters)
print(numbers)







