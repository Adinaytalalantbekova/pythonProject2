class Human:
    def __init__(self, name, age, heigth, gender ):
        self.my_name = name
        self.age = age
        self.heigth = heigth
        self.gender = gender

    def __str__(self):
        return f'Name: {self.my_name}\n'\
               f'Age:{self.age}\n'\
               f'Heigth:{self.heigth}\n'\
               f'Gender: {self.gender}\n'

class Programmer(Human):
    def __int__(self, name, age, heigth, gender, language, fast_typing, logic):
        super().__init__(name, age, heigth, gender)
        self.language = language
        self.fast_typing = fast_typing
        self.logic = logic
    def can_feeely_use_laptop(self):
        print("Yeap, I can freely use laptop like a God")

    def __str__(self):
        return f'Languages:{self.language}\n'\
               f'Fast Typing: {self.fast_typing}\n'\
               f'Logic: {self.logic}'

    def can_calculate(self, number_1, number_2):
        summary = number_1 + number_2
        return summary

    def can_say_hello(self):
        return 'Hello World'

human_1 = Human(name='adi', age=17, heigth=60,gender="male")
human_2 = Human('Adi', 20, 179, 'famale')
print(human_1.can_calculate(int(input('First: ')), int(input('second: '))))
print(human_2.can_say_hello())

print(human_2, human_1)
proger = Programmer(Language='Python',
                    fast_typing=True, logic_thinking=True,
                    name='adi', age=17, heigth=160,
                    gender='male')
print(proger)


