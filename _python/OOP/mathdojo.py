def varargs(arg1, *args):
    for a in args:
        print(a)
varargs("one", "two", "three") # output: two, three (on separate lines)


class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        # your code here
        for i in nums:
            self.result += i
        self.result = self.result + num
        # print(self.result)
        return self

    def subtract(self, num, *nums):
        sum = 0
        for i in nums:
            sum += i
        self.result -= ( num + sum)
        print(self.result)
        
        return self
        # your code here
# create an instance:
md = MathDojo()
# to test:

# x= md.subtract(2).subtract(2,5,1).subtract(13,2).result
# x= md.add(2).add(2,5,1).add(13,2).result
x = md.add(2).add(2,5,1).subtract(3,2).result

print(x)	# should print 5
# run each of the methods a few more times and check the result!


