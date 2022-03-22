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
    print(t)
    return t

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


game()


