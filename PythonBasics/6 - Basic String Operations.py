test1 = "Hello world!"
test2 = 'Hello world!'

# GET STRING LENGTH
print(str(len(test1)) + ' characters long')

# GET CHARACTER INDEX
print('"o" located at index ' + str(test1.index('o')))

# GET CHARACTER COUNT
print("l occurs " + str(test1.count("l")) + ' times')

# GET CHARACTERS FROM INDEX 3 - 7
print("Characters from index 3 - 7: " + str(test1[3:7]))

# GET CHARACTERS FROM INDEX 0 - 8, GETTING EVERY 3RD CHARACTER ( 'h' el 'l' o  'w')
print("Characters from index 0 - 8, skipping every 3rd character: " + str(test1[0:8:3]))

# GET STRING BACKWARDS
print("String backwards: " + str(test1[::-1]))

# CHECK IF STRING STARTS WITH SEQUENCE OF CHARACTERS. (CASE SENSITIVE)
print("test1 starts with 'hello': " + str(test1.startswith('Hello')))
print("test1 starts with 'test': " + str(test1.startswith('test')))

# SPLITS STRING INTO LIST ON CERTAIN STRING 
afewwords = test1.split(' ')
print(afewwords)


s = "Hey there! What should this string be?"

print('\n\n' + s)
print("Length of s = %d" % len(s))
print("The first occurence of the letter a = %d" % s.index("a"))
print("a occurs %d times" % s.count("a"))
print("the first five characters are '%s'" % s[:5])
print("the next five characters are '%s'" % s[5:10])
print("The thirteenth character is '%s'" % s[13])
print("the characters with odd index are '%s'" % s[1::2])
print("The last five characters are '%s'" % s[-5:])

print("String in uppercase: %s" % s.upper())

if s.startswith('Str'):
    print("String ends with 'Str'. Good!")
if(s.endswith('ome!')):
    print("String ends with 'ome!'. Good!")

print('Split the words of the string: %s' % s.split(' '))