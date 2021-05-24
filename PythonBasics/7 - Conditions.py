# BASIC COMPARISONS
# 
# AND
if True and False:
    print("1 True")
else:
    print("1 False")

# OR
if True or False:
    print("2 True")
else:
    print("2 False")

# IS
if True is True:
    print("3 True")
    
# IN
aList = ['Chris', 'Ben']
if 'Justin' in aList:
    print("lennyface")
elif 'Chris' in aList:
    print('chris in alist')

# EQUALS
if 2 == 2:
    print('4 True')

# EQUALS - LIST
if [1,2,3] == [1,2,3]:
    print('5 True')

if [1,2,3] is [1,2,3]:  # Looks to see if object occupies the same space in memory (reference vs. value)
    print('5 True 2')


# NOT
if True not False:
    print('6 True')
else:
    print('6 False')

