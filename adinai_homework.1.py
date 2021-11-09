class Animal:
    def __init__(self, name, age, color, appearance, food):
        self.name = name
        self.age = age
        self.color = color
        self.appearance = appearance
        self.food = food

    def __str__(self):
        return f'Name: {self.name}\n' \
               f'Age: {self.age}\n' \
               f'Color: {self.color}\n' \
               f'appearance: {self.appearance}\n' \
               f'food: {self.food}\n' \


class Zoo(Animal):
    def __init__(self, name, age, color, appearance, food, width, height, square, action):
        super().__init__(name, age,color, appearance, food)
        self.width = width
        self.height = height
        self.square = square
        self.action = action

    def __str__(self):
        return f'width: {self.width}\n'\
                f'heigt: {self.height}\n'\
                f'square: {self.square}\n'\

class ZooShow:
    def __init__(self,zoo):
        self.zoo = zoo
        self.ticket = 0
        if zoo.name == "masha":
            self.ticket = 50
    def getticket(self):
        return f"Цена на билет {self.ticket}$"
    def gatNameandAction(self):
        return f"Имя животного: {self.zoo.name}, {self.zoo.action}"


hare = Animal(name= 'Hare', age='3 months', color= 'white', appearance= 'cute',food='carrot')
wolf = Animal(name='wolf', age='1 year', color='gray', appearance='scary', food='meat')
lion = Animal(name='lion', age=' 4 year', color='oreng', appearance='passionate', food='meat')
cat = Animal(name='masha', age='7 months', color='white', appearance='very cute', food='milk')

cage_hera = Zoo(name='hera', age='3year',color="black", appearance="cute", food="carrot",width=2, height=2, square=4, action="Она высоко прыгает")
cage_wolf = Zoo(name='wolf', age='1 year', color='gray', appearance='scary',food='meat',width=10, height=10, square=100, action="Страшно пугает")
cage_lion = Zoo(name='lion', age='4 year', color="oreng", appearance='passionate',food='meat',width=10, height=10, square=100, action="Крик у него на высшем уровне")
cage_cat = Zoo(name='masha', age='7 months', color="white", appearance='very cute',food='milk',width=10, height=10, square=100,action='Она умеет разгаваривать')

catshow = ZooShow(zoo=cage_cat)
print(catshow.getticket())








