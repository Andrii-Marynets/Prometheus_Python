arr = [1, 2, 1, 1, 3, 4, 5, 4, 6, '2', 7, 8, 9, 0, 1, 2, 3, 4, 5]

def clean_list(list_to_clean):
    new_list = []
    j_list = list_to_clean[1:]
    for i in list_to_clean:
        ne = True
        for j in new_list:
            if i == j and type(i) == type(j):
                ne = False
        if ne == True:
            new_list.append(i)
    return new_list

print clean_list(arr)
