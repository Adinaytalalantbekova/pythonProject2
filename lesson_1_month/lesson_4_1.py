#plov = {'рис', 'мясо',  'морковь'}
#beshbarmak = {'мясо', 'лапша', 'лук'}

#print(plov & beshbarmak)
#print(plov.intersection(beshbarmak))

#print(plov | beshbarmak)
#print(plov.union(beshbarmak))

#print(plov - beshbarmak)
#print(plov.difference(beshbarmak))

#print(plov ^ beshbarmak)
#print(plov.symmetric_difference(beshbarmak))


menu = {
    'plov': {'рис', 'мясо',  'морковь'},
    'beshbarmak': {'мясо', 'лапша', 'лук'}
    'kasha': {'крупа','молоко','масло'}
}
guest = input('Choose: ')

for designation, ingridients in menu.items():
    if  guest == designation:
        print(designation, ingridients)
    elif guest in designation:
        print(designation, ingridients)

    else:
        print('goodbuy')
