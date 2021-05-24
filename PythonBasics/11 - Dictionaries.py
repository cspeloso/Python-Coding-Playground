# region SETTING INDIVIDUAL VALUES

print("Setting individual values: ")
phonebook = {}
phonebook["John"] = 4015550100
phonebook["Jack"] = 4015550150
phonebook["Jill"] = 4015550200
print(phonebook, end='\n\n')

# endregion

# region ALTERNATIVE WAY TO INITIALIZE A DICTIONARY

print('Setting individual values (alternative way)')

phonebook = {
    "John": 4015550100,
    "Jack": 4015550150,
    "Jill": 4015550200
}
print(phonebook)

# endregion

# region ITERATING OVER DICTIONARIES

print('\nIterating over dictionaries')

for name, number in phonebook.items():
    print("Phone number of %s is %s" % (name, number))
print()

#endregion

#region REMOVING A VALUE

print('Removing a value')
del phonebook['John']
print(phonebook, end='\n\n')

# endregion

# region ALTERNATIVE WAY TO REMOVE A VALUE

print('Removing a value (alternative way)')
phonebook.pop('Jack')
print(phonebook, end='\n\n')

phonebook = {"John" : 938477566, "Jack" : 937377264, "Jill" : 947662781 }

#endregion

# region EXERCISE

phonebook = {"John" : 938477566, "Jack" : 937377264, "Jill" : 947662781 }

phonebook['Jake'] = 4015556969
phonebook.pop('Jill')

if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")
if "Jill" not in phonebook:
    print("Jill is not in the phonebook.")

# endregion