savings = int(input(f'сумма:'))
interest = int(input(f'Процент:')) / 100
time = int(input(f'Время:'))

def calc_savings (savings,interest,time):
    for op in range(time):
        savings += savings * interest
    return savings

def bank(s,i=0.02,t=1):
    if i > 0.05:
        print(f'Максимальный процент 5%')
        return False
    
    savings = calc_savings(s,i,t)
    return savings


    

    

total_sav = bank(savings, interest, time)

if total_sav:

    print(f'Ваш счет в банке {total_sav}')
