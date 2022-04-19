def apply_to_each(L,f):
    for i in range(len(L)):
        L[i] = f(L[i])
numbers = [1, 0, 3.16,-2]
# apply_to_each(numbers, abs)
# print(numbers)
# apply_to_each(numbers, int)
# print(numbers)
# apply_to_each(numbers, float)
# print(numbers)
# apply_to_each(numbers, str)
# print(numbers)
def change_direction(d):
    return d *  -1

apply_to_each(numbers, change_direction)

def square(x):
    return x * x

print(numbers)