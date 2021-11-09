# Основные принципы ООП. наследование
class Junior:
    def __init__(self, language, soft_skills, laptop, salary):
        self.languege = language
        self.soft_skills = soft_skills
        self.laptop = laptop
        self.salary = salary


    def __str__(self):
        return f'language: {self.languege}\n'\
               f'soft_skills: {self.soft_skills}\n'\
                f'laptop: {self.laptop}\n'\
                f'salary: {self.salary}'

junior_1 = Junior(language='Python',
                  soft_skills='Good Enough',
                  laptop='gaming laptop',
                  salary='300$')

print(junior_1)

class Middle(Junior):
    def __init__(self, language, soft_skills, laptop, salary, fast_resolving, reliable):
        super().__init__(language, soft_skills, laptop, salary)
        self.fast_resolving = fast_resolving
        self.reliable = reliable

    def say_which_language(self):
        return f'Im using {self.languege}'


    def __str__(self):
        return super(Middle, self).__str__() + f'\nresolving: {self.fast_resolving}\n' \
                                               f'reliable: {self.reliable}'

middle_1 = Middle(language='Python',
                  soft_skills='Good Enough',
                  laptop='gaming laptop',
                  salary='300$',
                  fast_resolving='Often',
                  reliable=True)


print(middle_1.say_which_language())
print(middle_1)

class Senior(Middle):
    def __init__(self, language, soft_skills, laptop, salary, fast_resolving, reliable, architecture, leading_skill):
        super().__init__(language, soft_skills, laptop, salary, fast_resolving, reliable)
        self.architecture = architecture
        self.leading_skill = leading_skill

    def __str__(self):
        return super(Senior, self).__str__() + f'\nArchitecture: {self.architecture},' \
                                               f'Leading_skill: {self.leading_skill})'

senior = Senior(language='Python',
                soft_skills='Good Enough',
                laptop='gaming laptop',
                salary='6000$',
                fast_resolving='Often',
                reliable=True,
                architecture=True,
                leading_skill=True)

print(senior)






