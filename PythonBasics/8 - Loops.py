primes = [2,3,5,7]

# region FOR LOOPS
print('Primes: \t\t', end='')
for prime in primes:
    print(str(prime), end=' ')

print('\nRange 8: \t\t', end='')
for x in range(8):
    print(str(x), end=' ')

print('\nRange 3,8: \t\t', end='')
for x in range(3,8):
    print(str(x), end=' ')

print('\nRange 3,8 step 2: \t', end='')
for x in range(3,8,2):
    print(str(x), end=' ')

#endregion


# region WHILE LOOPS
count = 0

print('\n\nWhile count < 5')
while count < 5:
    print(count, end=' ')
    count += 1
#endregion


# region BREAK STATEMENT
count = 0

print('\n\nWhile loop using break')

while True:
    print(count, end=' ')
    count += 1
    if count >= 5:
        break
#endregion


# region CONTINUE STATEMENT 
# If this is hit in a loop, it will move to the next iteration without executing the rest of the current iteration of the loop.
# In the example below, when x is divisible by 2 it will move to the next iteration without hitting the "print(x)" line.
print('\n\nFor loop using continue')
for x in range(10):
    if x % 2 == 0:
        continue
    print(x, end=' ')
#endregion


# region ELSE (LOOPS)
#
# When a condition for a 'for' or 'while' loop fails, the 'else' clause will be executed.
# If a loop is broken out of using a break statement, the code contained in the 'else' clause will not be executed.
count = 0
print('\n\nWhile loop using else')
while count < 5:
    print(count, end=' ')
    count += 1
else:
    print('\ncount value reached %d' % count)

print('\nFor loop using else')
for i in range(1,10):
    if(i % 5 == 0):
        break
    print(i, end=' ')
else:
    print('this is not printed because for loop is terminated with break')

print('\nThe else clause when used with loops operates similarly to the FINAL statement from C#')
for i in range(1,3):
    print(i, end=' ')
else: 
    print('FINISHED')
#endregion


# region RANDOM EXAMPLE
numbers = [951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
           615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
           386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
           399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
           815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
           958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
           743, 527]

for x in numbers: 
    if x == 237:
        break
    if(x % 2 == 1):
        continue

    print(x, end=' ')
#endregion