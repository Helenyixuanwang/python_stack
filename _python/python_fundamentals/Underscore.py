class Underscore:

#Map. Produces a new array of values by mapping each value in list through a transformation function
    def map(self, iterable, callback): #map work
        new_arr=[]
        for i in range(len(iterable)):
            new_arr.append(callback(iterable[i]))
        return new_arr

#Find. Looks through each value in the list, returning the first one that passes a truth test    
    def find(self, iterable, callback): # find work
        for val in iterable:
            if callback(val):
                return val
    
#filter: looks through each value in the list, returning an array of all the values that pass a truth test 
    def filter(self, iterable, callback):
        new_arr=[]
        for val in iterable:
            if callback(val):
                new_arr.append(val)
        return new_arr


#Returns the values in list without the elements that the truth test (predicate) passes.
    def reject(self, iterable, callback):
        new_arr=[]
        for val in iterable:
            if callback(val)==False:
                new_arr.append(val) 
                
        return new_arr
        # your code
# you just created a library with 4 methods!
# let's create an instance of our class
_ = Underscore() 
maps = _.map([2,3,4,5,6], lambda x: x*2)
print(maps)

x = _.find([2,4,7,9,10], lambda i : i >6)
print(x)

arr = _.filter([2,5,7,9,10,13,19], lambda j : j % 2 ==1 )
print(arr)

arr2 = _.reject([1,3,5,4,6,9,14,18,-1], lambda x: x > 2 )
print(arr2)