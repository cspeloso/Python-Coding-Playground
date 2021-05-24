# MATH
#
# ADDITION
print("ADDITION: \t\t" + str(1 + 2))

# SUBTRACTION
print("SUBTRACTION: \t\t" + str(1 - 2))

# MULTIPLICATION
print("MULTIPLICATION: \t" + str(2 * 3))

# DIVISION
print("DIVISION: \t\t" + str(6 / 4))

# REMAINDER
print("REMAINDER: \t\t" + str(11 % 3))

# SQUARED
print("SQUARED: \t\t" + str(7 ** 2))

# CUBED
print("CUBED: \t\t\t" + str(2 ** 3) + "\n")


# LISTS OF NUMBERS
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]

# ADDING TWO LISTS
all_numbers = odd_numbers + even_numbers
print(all_numbers)

# MULTIPLYING A LIST
print([1,2,3] * 3)

x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 10
big_list = [x,y] * 10

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

if(x_list.count(x) == 10 and y_list.count(y) == 10):
    print("Almost there...")
if(big_list.count(x) == 10 and big_list.count(y) == 10):
    print("Great!\n")



# STRINGS
helloworld = "hello" + " " + "world "
print(helloworld)

lotsofhelloworlds = helloworld * 10
print(lotsofhelloworlds)







