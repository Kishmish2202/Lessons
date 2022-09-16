text = "'Ура!', — вопите, дети, повару"


def convert(w):
    yes = 'ёйцукенгшщзхъэждлорпавыфячсмитьбю'
    gg = ''
    for i in w.lower():
        for r in yes:
            if i == r:
                gg += i
    return gg
print(convert(text))

def palindrome(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and palindrome(s[1:-1])
a = palindrome(convert(text))
print(a)


        