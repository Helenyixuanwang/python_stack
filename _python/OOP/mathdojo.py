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
            self.result = self.result+ i
        self.result = self.result + num
        print(self.result)
        return self

    def subtract(self, num, *nums):
        for i in nums:
            self.result =self.result+ i
        self.result = 0-( num + self.result)
        return self
        # your code here
# create an instance:
md = MathDojo()
# to test:
x = md.add(3,2).result
print(x)	# should print 5
# run each of the methods a few more times and check the result!


