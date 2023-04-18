def mask24(lst):
    result = []
    for elem in lst:
        if elem[-2:] == '24':
            result.append(elem)
        else:
            continue
    return result

mylist = ['192.168.0.5/24', '172.16.0.1/25', '10.10.10.12/24', '192.168.1.12/24']
print(mylist)
print('список ip адресов с 24 маской')
print(mask24(mylist))