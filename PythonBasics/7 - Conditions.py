# BASIC COMPARISONS
# 
# AND
if True and True:
    print("1 True")

# OR
if True or False:
    print("2 True")

# IS
if True is True:
    print("3 True")
    
# IN
aList = ['Chris', 'Ben']
if 'Justin' in aList:
    print("lennyface")
elif 'Chris' in aList:
    print('4 True')

# EQUALS
if 2 == 2:
    print('5 True')

# EQUALS - LIST
if [1,2,3] == [1,2,3]:
    print('6 True')

if [1,2,3] is [1,2,3]:  # Looks to see if object occupies the same space in memory (reference vs. value)
    print('6.1 True')


# NOT (logical NOT operator; ! equivalent)
if not False:
    print('7 True')


# GREATER THAN
if 3 > 2:
    print('8 True')

if 2 < 3:
    print('9 True')

if True and len('testing') > 4:
    print('10 True')

if 0 and True:
    print('11 True')
elif 1 and True:
    print('11.1 True')