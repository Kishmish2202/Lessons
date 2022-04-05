from random import randint
c = randint(1,100)
print('Угадайте число')
while True:
    uno = int(input('Ваше предположение:'))
    if c != uno:
        if c > uno:
            print(f'Попробуйте число больше {uno}')
        elif c < uno:
            print(f'Попробуйте число меньше {uno}')
    else:
        print('Вы угадали!')
        break

