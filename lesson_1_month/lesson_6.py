words = ['kg', 'kz', 'ru', 'ua','gb']
names = ['adil','samat','erkin']
# #
# # def up_l(word):
# #         return word.upper()
# # def edit_f(lst, funk):
# #     for word in lst:
# #         print(funk(word))
# # # edit_l(words, up_l)
# # edit_f(names, up_l)
#
edit_l = list(map(lambda word: word.upper(), words))
print(edit_l)
print(list(map(lambda word: word.upper(), names)))
print()



# a = lambda a, b: a + b
# print(a(2, 3))
#
# print(10 + (lambda x: x ** 2)(2))
#
# b = (lambda x, y=2: x + y)(4,6)
# print(b)




