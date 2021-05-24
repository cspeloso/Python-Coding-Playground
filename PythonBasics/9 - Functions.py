#region Regular Function Declaration
def my_function():
    print("Hello from my function!")
my_function()
#endregion

#region Function Declaration with Arguments
def my_function_with_args(username, greeting):
    print("%s %s! From my function!" % (greeting, username))
my_function_with_args("Chris", "Greetings")
#endregion

#region Function with a return declaration
def sum_two_numbers(a, b):
    return a + b
print(sum_two_numbers(1,2))
#endregion

#region Function with a list return
def list_benefits():
    return "More organized code", "More readable code", "Easier code reuse"
print(list_benefits())
print(list_benefits()[1], end='\n\n')
#endregion

#region Function with a loop
def name_the_benefits_of_functions(benefits):
    for benefit in benefits:
        print("%s is a benefit of functions!" % benefit)
name_the_benefits_of_functions(list_benefits())
#endregion