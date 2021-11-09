class Car:
    def __int__(self, brand, color, type_car):
        # amount_passenger, max_speed,
        # engine, country, year, mechanic):
        self.brand = brand
        self.color = color
        self.type_car = type_car
        # self.amount_passenger = amount_passenger
        # self.max_speed = max_speed
        # self.engine = engine
        # self.country = country
        # self.year = year
        # self.mechanic = mechanic

        # self.brand = brand
        #
        # if isinstance(color, str):
        #     self.color = color
        # else:
        #     raise ValueError('Color should be string!')
        # if isinstance(type_car, str):
        #     self.type_car = type_car
        # else:
        #     raise ValueError('Type Car should be string!')
        #
        # if isinstance(amount_passenger, int):
        #     self.amount_passenger = amount_passenger
        # else:
        #     raise ValueError('Amount Passenger should be integer!')
        # if isinstance(max_speed, int):
        #     self.max_speed = max_speed
        # else:
        #     raise ValueError('Max Speed should be integer!')
        # if isinstance(engine, float):
        #     self.engine = engine
        # else:
        #     raise ValueError('Engine should be float!')
        # if isinstance(country, str):
        #     self.country = country
        # else:
        #     raise ValueError('Country should be string!')
        # if isinstance(year, int):
        #     self.year = year
        # else:
        #     raise ValueError('Year should be integer!')
        # if isinstance(mechanic, str):
        #     self.mechanic = mechanic
        # else:
        #     raise ValueError('Mechanic should be string!')

    def tunning(self, cost):
        car_cost = 1000
        summery = car_cost + cost
        return summery

    def __str__(self):
        return f'{self.brand}, {self.color}, ' \
               f'{self.type_car}'

        # f'{self.year}, {self.country}, {self.amount_passenger},' \
        # f'{self.max_speed}, {self, self},{self.engine},{self.mechanic}, ' \


car_car = Car()
print(car_car)
# print(car_1.tunning(80000))
# +
#
