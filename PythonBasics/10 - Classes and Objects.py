#region CLASS DECLARATION

# Defines a class
class MyClass:

    # Declares a class parameter (variable)
    variable = 'blah'

    # Declares a class method (function)
    def function(self):
        print('This is a message from inside the class')

# Declares an object
x = MyClass()
y = MyClass()
y.variable = "TEST!"

# Accessing object parameter
print(x.variable)
print(y.variable)

# Accessing object method
x.function()

#endregion


#region EXAMPLE

class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00

    def description(self):
        return "%s is a %s %s worth $%.2f" % (self.name, self.color, self.kind, self.value)

car1 = Vehicle()
car1.name = "Hyundai"
car1.color = "white"
car1.value = 150.00

car2 = Vehicle()
car2.name = "Honda"
car2.color = "gray"
car2.value = 20000

print(car1.description())
print(car2.description())

#endregion