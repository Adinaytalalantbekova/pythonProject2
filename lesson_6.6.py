words = ['kg', 'kz', 'ru', 'ua','gb']
names = ['adil','samat','erkin','max','azamat','abdraim']

edit_l = list(map(lambda word: word.upper(), words))
print(edit_l)
print(list(map(lambda word: word.upper(), names)))

filter_names = list(filter(lambda word: not word.startswitw ('a') and names))
#
# print(filter_names)


names = ['adil','samat','erkin','max','azamat','abdraim']
# filter_names = list(filter(lambda word: not word.startswitw ('a'), names))
# print(filter_names)

def index_list (lst):

    while True:
        try:
            position = int(input('Вводите индекс'))
            print(names[position])
        except IndexError:
            print(f'Вводите от 0 до{len(lst)-1}')
        except:
            print('Вы ввели совсем не то!')

index_list(filter_names)


from random import randint
print(randint(1,23))









