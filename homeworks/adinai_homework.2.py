# Number 1
class Grandad:
    def __init__(self, name, age, height, appearance):
        self.name = name
        self.age = age
        self.height = height
        self.appearance = appearance

    def __str__(self):
        return f'Name: {self.name}\n' \
               f'Age: {self.age}\n' \
               f'Height: {self.height}\n' \
               f'Appearance: {self.appearance}'


granddad = Grandad(name='Osmon',
                   age=85,
                   height=165,
                   appearance='old')

print(granddad)


class Dad(Grandad):
    def __init__(self, name, age, height, appearance, work):
        super().__init__(name, age, height, appearance)
        self.work = work

    def my_dad(self):
        return f'это мой папа: {self.name}'

    def __str__(self):
        return super(Dad, self).__str__() + f'\nWork: {self.work}'


dad = Dad(name='Talant',
          age=50,
          height=170,
          appearance="old man",
          work='no worker')

print(dad.my_dad())
print(dad)


class Son(Dad):
    def __init__(self, name, age, height, appearance, work, color_eye):
        super().__init__(name, age, height, appearance, work)
        self.color_eye = color_eye

    def my_love_dad(self):
        return f'Это мой любимый папа: {self.name}'

    def __str__(self):
        return super(Son, self).__str__() + f'\nColor eye: {self.color_eye}'


son = Son(name='Myrza',
          age=15,
          height=165,
          appearance='young',
          work='farmer',
          color_eye='green')

print(son.my_love_dad())
print(son)





# Number 2

class Favorit_book:
    def __init__(self, author, year, content, view):
        self.author = author
        self.year = year
        self.content = content
        self.view = view

    def __str__(self):
        return f'Author: {self.author}\n' \
               f'Year: {self.year}\n' \
               f'Content: {self.content}\n' \
               f'View: {self.view}'

    def __essense(self):
        print("Подмознание может всё!")

    def _essense(self):
        print('Закладка мыслей')


book_1 = Favorit_book(author="Djon Keho",
                      year=2019,
                      content="Иной взгляд на реальность",
                      view="Интересный, полезный")

print(book_1)
# print(book_1._essense())
# print(book_1.__essense())



# Number 3

class Warrior:
    def __init__(self, name, age, weapon):
        self.name = name
        self.age = age
        self.weapen = weapon

    def __str__(self):
        return f'Name: {self.name}\n' \
               f'Age: {self.age}\n' \
               f'Weapon: {self.weapen}'

    def attack(self):
        print('Удар мечом ')


warrior = Warrior(name='Cэндзи Мурамаса', age=32, weapon="Мечь")

print(warrior)
print(warrior.attack())


class Renger:
    def __init__(self, name, age, weapon):
        self.name = name
        self.age = age
        self.weapen = weapon

    def __str__(self):
        return f'Name: {self.name}\n' \
               f'Age: {self.age}\n' \
               f'Weapon: {self.weapen}'

    def attack(self):
        print("Выстрел из лука")

renger = Renger(name='Кевин', age=36, weapon='Луч')

print(renger)
print(renger.attack())


class Wizard:
    def __init__(self, name, age, weapon):
        self.name = name
        self.age = age
        self.weapen = weapon

    def __str__(self):
        return f'Name: {self.name}\n' \
               f'Age: {self.age}\n' \
               f'Weapon: {self.weapen}'

    def attack(self):
        print("Читать волшебные заклинания")

wizard = Wizard(name='Геллерт Гриндевальд', age=45, weapon="книга: Огненный Шар")

print(wizard)
print(wizard.attack())





# Number 4

class Doctor:
    def __init__(self, name, age, work, place_of_work):
        self.name = name
        self.age = age
        self.work = work
        self.plase_of_work = place_of_work

    def __str__(self):
        return f'Name: {self.name}\n' \
               f'Age: {self.age}\n' \
               f'Work: {self.work}\n' \
               f'Place of work: {self.plase_of_work}'

    def work1(self):
        print("Вылечит людей")

docror = Doctor(name='Ави Хафец', age=50, work="Хирург", place_of_work='В Больнице')

print(docror)
print(docror.work1())


class Programmer(Doctor):
    def __init__(self, name, age, work, place_of_work):
        super().__init__(name, age, work, place_of_work)

    def work1(self):
        print("Создает код")

programmer = Programmer(name="Тим Бернерс-Ли", age=57, work="Программист", place_of_work="В офисе")

print(programmer)
print(programmer.work1())

class Salesman(Programmer):
    def __init__(self, name, age, work, place_of_work):
        super().__init__(name, age, work, place_of_work)

    def work1(self):
        print("Продает товары")

salesman = Salesman(name='Гулайым', age= 35, work="продовец", place_of_work="В магазине")

print(salesman)
print(salesman.work1())







