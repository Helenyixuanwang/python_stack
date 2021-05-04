
def insert(arr):
    temp = arr[0]
    for i in range(1,len(arr)):
        
        for j in range(0,i):
            if arr[j]>arr[i] and i-j>=1:
                temp=arr[i]
                k = i-1
                while k >= j and k <=i:
                    arr[k+1]=arr[k]
                    k=k-1
                arr[j]=temp
            
    return arr

print(insert([5,1,4,2,-1,3]))
