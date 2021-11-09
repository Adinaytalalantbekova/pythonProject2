def zodiac(day, month, name='name'):
    print(name)
    if (day >= 21 and day <=31 and month == 3) or (day >= 1 and day <= 20 and month == 4):
        print('Овен')
    elif (day >= 21 and day <=30 and month == 4) or (day >= 1 and day <= 21 and month == 5):
        print('Телец')
    elif (day >= 22 and day <=31 and month == 5) or (day >= 1 and day <=21 and month == 6):
        print('Блезнецы')
    elif (day >= 22 and day <=30 and month == 6) or (day >= 1 and day <= 22 and month == 7):
        print('Рак')
    elif (day >= 23 and day <= 31 and month == 7) or (day >= 1 and day <= 21 and month == 8):
        print('Лев')
    elif (day >= 22 and day <= 31 and month == 8) or (day >= 1 and day <= 23 and month == 9):
        print('Дева')
    elif (day >= 24 and day <=30 and month == 9) or (day >= 1 and day <= 23 and month == 10):
        print('Весы')
    elif (day >= 24 and day <= 31 and month == 10) or (day >= 1 and day <=22 and month == 11):
        print('Скорпион')
    elif (day >= 23 and  day <= 30 and month == 11) or (day >= 1 and day <=22 and month == 12):
        print('Стрелец')
    elif (day >= 23 and day <= 31 and month == 12) or (day >= 1 and day <=20 and month == 1):
        print('Козерок')
    elif (day >= 21 and day <=30 and month == 1) or (day >= 1 and day<=19 and month == 2):
        print('Водолей')
    elif (day >= 20 and day <=28 and month == 2) or (day >= 1 and day <= 20 and month == 3):
        print('Рыбы')
zodiac(89,5, "adi")