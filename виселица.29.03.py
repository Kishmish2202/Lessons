def welcome_speech(t):
    print(f'''
    Добро пожаловать в игру - Hangman 2000
    Ваша задача угадать загаданное слово за несколько попыток
    иначе вас ждет расплата!
    Загаданное слово состоит из {len(t)} букв {t}
    ''')

def start_template(w):
    t = []
    for l in w:
        t.append('_')
    return t

def check_mistake(w,g):
    flag = False
    for i in w:
        if i == g:
            flag = True
    return flag

def list_to_string_convert(t):
    s = ''
    return s.join(t)

def get_world(w):
    return w[0]

def user_input():
    return input('Введите букву: ')

def build_template(t, w, g=''):
    for i in range(len(w)):
        if t[i] == '_':
            if w[i] == g:
                t[i] = w[i]
            else:
                t[i] = '_'
    return t

def check_attempt(lifes):
    lifes -= 1
    return lifes

def check_win(g):
    for i in g:
        if i == '_':
            return True
    return False

def lose_speech():
    print(f'Вы проиграли!')

def win_speech():
    print(f'Вы выиграли! Ура!')
                


def print_result(g):
    print(f'Текущий результат: {g}')

def game():
    progress = True
    world = ['orange']
    lifes = 3

    world_in_play = get_world(world)
    template = start_template(world_in_play)
    welcome_speech(list_to_string_convert(template))

    while progress:
        user_quess = user_input()
        template = build_template(template,world_in_play,user_quess)
        quessed = list_to_string_convert(template)
        print_result(quessed)
        progress = check_win(quessed)

        if not check_mistake(world_in_play,user_quess):
            print(f'осталось {lifes} попыток')
            lifes = check_attempt(lifes)
        if lifes == 0:
            lose_speech()
            break
        if not progress:
            win_speech()
game()
