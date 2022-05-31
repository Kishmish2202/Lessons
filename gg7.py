def count(n):
   gg = [1,1]
   for i in range(n - 2):
      c = gg[-1] + gg[-2]
      gg.append(c)
   return gg[-1]
#print(count(7))

# def fib(n):
#     if n == 1 or n == 0:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

print(count(36))