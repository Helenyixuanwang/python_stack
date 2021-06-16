def contain(lst, value):
    for x in range(len(lst)):
        if lst[x]!= value:
            continue
        if x < len(lst):
            return True
        else:
            return False
           


print(contain([1,3,5,7], 1))