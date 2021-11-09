members = [
    {'name':'Azat', 'age': 18, 'height': 185, 'physic':True},
    {'name':'Adilet', 'age': 17, 'height': 180, 'physic':False},
    {'name':'Asan', 'age': 20, 'height': 179, 'physic':True},
]
soldiers = []
def selection_army(member_lst):
    for member in member_lst:
        if member['age'] >= 18 and member['height'] >= 180 and member ['physic'] == True:
            member['soldier'] = True
            soldiers.append(member)
    print(soldiers)
def add_member(name, age, height, physic):
    return {'name': name, "age": age, "height":  height, 'physic': physic}
members.append(add_member('Ulan',19, 181, True))
selection_army(members)
def find (name: str, lst):
    for member in lst:
        if member ['name'] == name.title():
            return member
    print('объект не найден')
print(find("Adilet", members))
print(find('asan', soldiers))
