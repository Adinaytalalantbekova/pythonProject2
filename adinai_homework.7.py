import random, time
rnd = 0
guessnum = random.randint(1, 100)
start = time.time()
while True:
    rnd += 1
    try:
        guess = int(input('Угадай число:  (> - меньше, < - больше)'))
        if guess > 100 or guess < 1:
            print('между 1 и 100')
            continue
    except:
        print('нельза вводить буквы')
        continue
    if (guess > guessnum):
        if guess - guessnum <= 5:
            print('очень близко')
        elif guess - guessnum <= 10:
            print('близко')

        print('Это больше чем загаданное ')
    if (guess < guessnum):
        if guessnum - guess <=5:
            print('очень близко')
        elif guessnum - guess <= 10:
            print('близко')
        print('Это меньше чем загаданное ')
    if guessnum == guess:
        print('Вы отгадали число')
        print("количество попыток", rnd)
        print('время: ', round(time.time() - start), 'секунд')
        break
