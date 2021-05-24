# %s                        -> string
# %d                        -> int
# %f                        -> float
# %.<number of digits>f     -> floating point number with fixed digits.
# %x or %X                  -> integers in hex representation (lowercase/uppercase)
name = "John"
print("Hello, %s!" % name)

age = 23
print("%s is %d years old." % (name, age))

mylist = [1,2,3]
print("A list: %s" % mylist)

data = ("John", "Doe", 53.44)
format_string = "Hello"
print("%s %s %s. Your current balance is: $%.2f" % (format_string, data[0], data[1], data[2]))