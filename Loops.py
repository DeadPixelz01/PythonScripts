# An extremely basic "for" loop.
# Prints from the list 'primes'. 
print('Loop 1')
print('-------')
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)
print('\n')

# A few for loops that uses 'range'/'xrange'.
# Prints out the numbers 0,1,2,3,4,5.
print('Loop 2')
print('-------')
for x in range(5):
   print(x)
print('\n')

# Prints out all numbers between 3 and 6.
print('Loop 3')
print('-------')
for x in range(3, 6):
    print(x)
print('\n')

# Prints numbers 3, 5, 7.
print('Loop 4')
print('-------')
for x in range(3, 8, 2):
    print(x)
print('\n')


# An extremely basic "while" loop.
# Prints out 0,1,2,3,4
print('Loop 5')
print('-------')
count = 0
while count < 5:
    print(count)
    count += 1
print('\n')

# 'Break' and 'continue' statements.
# Prints out 0,1,2,3,4.
print('Loop 6')
print('-------')
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break
print('\n')

# Prints out only odd numbers (1,3,5,7,9).
print('Loop 7')
print('-------')
for x in range(10):
    # The following checks if the variable 'x' is even.
    if x % 2 == 0:
        continue
    print(x)
print('\n')

# Using 'else' statements.
# Unlike other langauges, Python allows you to use 'else' statements inside a loop.
# Prints out 0,1,2,3,4 and then prints out a message when the loop has reached the number 5.
print('Loop 8')
print('-------')
count = 0
while(count < 5):
    print(count)
    count += 1
else:
    print('count value reached %d' %(count))
print('\n')

# Prints out 1,2,3,4.
print('Loop 9')
print('-------')
for i in range(1, 10):
    if(i % 5 == 0):
        break
    print(i)
else:
    print('This is not printed because the for loop was terminated because of the break, not because there is an error within my source code =d')
print('\n')

