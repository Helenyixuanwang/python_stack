a, *b = [1,2,3,4,5]
print(a)
print(b)

a,b ='Jane','Alice'
a,b = b,a
print(a)
print(b)

def f(x,y,z):
    return x+y*z

#print(f(*[1,3,4]))
print(f(**{'z':4, 'x':1,'y':3}))