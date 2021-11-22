class Sort:
    def __init__(self, my_list: list):
        self.my_list = my_list

    def bubble_sort(self):
        swapped = False
        for i in range(len(self.my_list)-1, 0, -1):
            for j in range(i):
                if self.my_list[j] > self.my_list[j + 1]:
                    self.my_list[j], self.my_list[j + 1] = self.my_list[j + 1], self.my_list[j]
                    swapped = True
            if swapped:
                swapped = False
            else:
                break
        return self.my_list

    def __str__(self):
        return f'{self.my_list}'


sort = Sort(my_list=[3, 1, 81, 35, 22])

print(sort.bubble_sort())







