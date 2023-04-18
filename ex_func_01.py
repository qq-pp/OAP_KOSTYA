def unique(lst):
    result = []
    print(lst)
    for elem in lst:
        if elem in result:
            continue
        else:
            result.append(elem)
    return result

mylist = [1, 1, 2, 1, 3, 2, 3,4]
print(unique(mylist))