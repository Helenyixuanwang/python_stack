def findDuplicate(lst):
    seen=[]
    duplicate=[]
    for x in range(len(lst)):
        if x in seen:
            duplicate.append(lst[x])
        else:
            seen.append(lst[x])
    print("duplicate is ", duplicate)
    print("seen is ", seen)
    return duplicate

print(findDuplicate([1,2,1,4,3,2,3]))