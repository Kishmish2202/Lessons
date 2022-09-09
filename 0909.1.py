#def mult(a,b):
#    num = a
#    for i in range(b):
#        num += a
#    return num - a
#print (mult(3,2))

def fib(n):
    if n == 1 or n ==0:
        return 1
    else:
        return fib(n-1) + fib(n - 2)

print(fib(36))