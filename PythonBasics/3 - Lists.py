# CREATING A LIST WITH SPECIFIC VALUES
mylist = [1,2,3]

# CREATING AN EMPTY LIST
mylist = []

# ADDING VALUES TO A LIST
mylist.append(1)
mylist.append(2)
mylist.append(3)

# CALLING LIST VALUES BY INDEX
print("Calling list values by index: %s, %s, %s" % (mylist[0], mylist[1], mylist[2]))

# LOOPING THROUGH A LIST
print("Looping through a list: ", end='')
for x in mylist:
    print(str(x) + ' ', end='')
print("\n")

# SETTING LISTS OF SEVERAL VALUES
numbers = [1,2,3]
names = ["John", "Eric", "Jessica"]

# LISTS AND PRINTING
second_name = names[1]
print(numbers)
print(names)
print("The second name in the names list is %s" % second_name)