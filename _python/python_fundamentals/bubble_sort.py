def bubble(lst):
    for j in range(len(lst)-1):
        for i in range(len(lst)-1-j):
            if lst[i]>lst[i+1]:
                lst[i],lst[i+1]=lst[i+1],lst[i]

    print(lst)
    return(lst)

bubble([4,1,-9,10,9])