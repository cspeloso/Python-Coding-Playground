# INTEGERS
myint = 7
print(myint)

# FLOATS
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)

# STRINGS
mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)
mystring = "Don't worry about the apostrophes"
print(mystring)

# ADDING VARIABLES
one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = 'world'
print(hello + ' ' + world)

# SETTING MULTIPLE VARIABLES IN ONE LINE
a, b = 3, 4
print(a,b)


mystring = "hello"
myfloat = 10.0
myint = 20

# COMPARING VARIABLES
if mystring == hello:
    print("String: %s" % mystring)

# CHECKING VARIABLE TYPES
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if(isinstance(myint, int) and myint == 20):
    print("Integer: %d" % myint)
