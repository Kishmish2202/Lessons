def merge_dict(d_one, d_two):
    merged = {}
    for i in d_one:
        if i in d_two:
            merged[i] = [d_one[i]], [d_two[i]]
        else: 
            merged[i] = d_one[i]
    for i in d_two:
        if i not in d_one:
            merged[i] = d_two[i]
        return merged 






print(merge_dict({"А": 1, "С": 2}, {"Б": 2, "А": 4}))