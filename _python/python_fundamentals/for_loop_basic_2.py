#1.Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
#Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
def biggie(lst):
    for x in range(len(lst)):
        if list[x] > 0:
            list[x] = 'big'

    return lst

print(biggie([-1,3,5,-5]))

#2.Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
#Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
#Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
def countPositive(lst):
    count = 0
    for x in range(len(lst)):
        if lst[x] > 0:
            count = count+1

    lst[len(lst)-1] = count
    return lst

print(countPositive([1,-1,1,-1,1,-1]))

#3.Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
#Example: sum_total([1,2,3,4]) should return 10
#Example: sum_total([6,3,-2]) should return 7
def sum(lst):
    sum = 0
    for x in lst:
        sum = sum + x
    return sum

print(sum([6,3,-2]))

#4.Average - Create a function that takes a list and returns the average of all the values.
#Example: average([1,2,3,4]) should return 2.5
def average(lst):
    ave = 0
    sum = 0
    for x in lst:
        sum = x + sum

    ave = sum / len(lst)
    return ave

print(average([1,2,3,4]))

#5.Length - Create a function that takes a list and returns the length of the list.
#Example: length([37,2,1,-9]) should return 4
#Example: length([]) should return 0
def listLength(lst):# 
    count = 0
    for x in lst:
        count = count+1
    return count

print(listLength([37,2,1,-9]))

#6.Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
#Example: minimum([37,2,1,-9]) should return -9
#Example: minimum([]) should return False
def min(lst):
    
    if len(lst) == 0:#pay attention
        return False  #pay attention
    else:
        min = lst[0]
        for x in range(1,len(lst)):
            if min > list[x]:
                min = list[x]

        return min

#print(min([39,-10,1,9]))
print(min([]))

#7.Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
#Example: maximum([37,2,1,-9]) should return 37
#Example: maximum([]) should return False
def max(lst):
    
    if len(lst) == 0:
        return False  # return False but not print("False")
    else:
        max = lst[0]
        for x in range(1,len(lst)):
            if max < lst[x]:
                max = lst[x]

        return max

#print(max([39,-10,1,9]))
print(max([]))

#8.Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
#Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
def ultimate(lst):
    dic = {
        'sumTotal': None,  # I updated here after I read solutions from the platform !!!
        'average':None,
        'minimum':None,
        'maximum':None,
        'length':0
    }
    if len(lst)==0: # I updated here after I read solutions from the platform !!!
        return dic
    else:
        sum = 0
        ave = 0
        min = lst[0]
        max = lst[0]
        length = 0
        for x in lst:
            sum = sum + x
            if min > x:
                min = x
            elif max < x:
                max = x
            length += 1

    ave = sum /len(lst)
          
    dic["sumTotal"] = sum
    dic["average"] = ave
    dic["minimum"] = min
    dic["maximum"] = max
    dic["length"] = length
    return dic
    
    
print(ultimate([]))

#9.Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
#Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
def reverse(lst):  # why solution does not use temp to do this?
    temp = list[0]
    for x in range(int(len(lst)/2)):
        temp = list[x]
        list[x]= list[len(lst)-1-x]
        list[len(lst)-1-x]= temp

    return lst
print(reverse([37,21,7,5,-9]))



