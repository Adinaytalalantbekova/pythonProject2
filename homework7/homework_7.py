class Universal:
    def __init__(self, number):
        self.number = number

    def sort_num(self):
        self.number = str(self.number)
        for i in range(len(self.number)//2):
            if self.number[i] != self.number[len(self.number)-1-i]:
                return False
        return True

sort_number = Universal(number=1245421)
print(sort_number.sort_num())


