def find_num (array, num):
    for i in array:
        if i == num:
            ind = array.index(i)
            return True , ind
    return False , -1

print (find_num ([1,2,3,4,5], 10))