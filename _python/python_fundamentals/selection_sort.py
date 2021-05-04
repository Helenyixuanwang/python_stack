
#selection sort
def sele_sort(lst):
    
    temp = lst[0]
    for j in range(len(lst)-1):
        min =lst[j]
        for i in range(j,len(lst)):
            
            if min >= lst[i]:
                min= lst[i]
                index = i
        print("index is ", index)
        temp = lst[index]
        lst[index] = lst[j]
        lst[j]=temp
    print(lst)
    
    
#sele_sort([32,92,62,42,72,22,12])
sele_sort([-64, 25, -12, 22, 11])


#selection sort
def sele_sort(lst):
    
    temp = lst[0]
    for j in range(len(lst)):
        min = j # min is the pointer that points to minimum value of each iteration
        for i in range(j+1,len(lst)):
            
            if lst[min] >= lst[i]:
                min = i
        print("Index of minimum value is ", min)
        temp = lst[min]
        lst[min] = lst[j]
        lst[j]=temp
    print(lst)
    
    
#sele_sort([32,92,62,42,72,22,12])
sele_sort([64, 25, -12, 22, -12])
