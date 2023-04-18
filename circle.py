def evenCounter(lst):
    number = 0
    for x in lst:
        progres = x % 2
        if progres == 0:
            number += 1
    return number
mylist = [1,2,100,150,4,11,12]
evens = evenCounter(mylist)
print(evens)