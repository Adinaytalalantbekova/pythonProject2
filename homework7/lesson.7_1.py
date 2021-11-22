
class Sorted:
    def __init__(self, my_list):
        self.my_list = my_list

    def pratition(self, lst):
        if len(lst) <= 1:
            return lst

        element = lst[0]
        left = list(filter(lambda num: num < element, lst))
        center = [num for num in lst if num == element]
        right = list(filter(lambda num: num > element, lst))

        return self.pratition(left) + center + self.pratition(right)

    def quick_sort(self):
        if len(self.my_list) <= 1:
            return self.my_list

        element = self.my_list[0]
        left = list(filter(lambda num: num < element, self.my_list))
        center = [num for num in self.my_list if num == element]
        right = list(filter(lambda num: num > element, self.my_list))

        return self.pratition(left) + center + self.pratition(right)


sorted = Sorted(my_list=[3, 1, 81, 35, 22])

print(sorted)
print(sorted.quick_sort())