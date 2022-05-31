def find_uniq(x):
    count1 = []
    count2 = []
    for i in x:
        if i % 2 == 0:
            count1.append(i)
        else: 
            count2.append(i)
    if count1 > count2:
        return count1
    else:
        return count2







print(find_uniq([1,2,3]))
print(find_uniq([4,5,6]))