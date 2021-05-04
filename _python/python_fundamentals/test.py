class Underscore:
    def map(self, iterable, callback):
        new_list=[]
        for i in range(len(iterable)):
            new_list[i]=callback(iterable[i])
        return new_list

        # your code here
    def find(self, iterable, callback):
        for val in iterable:
            if callback(val):
                return val
        # your code here
    def filter(self, iterable, callback):
        new_list=[]
        for val in iterable:
            while callback(val):
                new_list.append(val)
        return new_list
        # your code
    def reject(self, iterable, callback):
        # your code
# you just created a library with 4 methods!
# let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable that is an underscore
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# should return [2, 4, 6] after you finish implementing the code above
