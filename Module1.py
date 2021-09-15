import random

"""create list of 100 random numbers from 0 to 1000"""
# Return and print 100 randomly selected values from 1 to 1000
res = [random.randrange(1, 1000) for i in range(100)]
print(f'List of random numbers\n{res}')

"""sort list from min to max (without using sort())"""
# previous value position in the list
for i in range(0, len(res)):
    # the next value position in the list
    for j in range(i + 1, len(res)):
        # comparing previous and next values: if previous value is bigger than the next value
        if res[i] > res[j]:
            # swap values
            res[i], res[j] = res[j], res[i]
print(f'List ordered:\n{res}')

"""calculate average for even and odd numbers"""
# empty list for odd numbers
odd_numbers = []

# empty list for even numbers
even_numbers = []

# for each value in the list
for i in res:
    # if value is even
    if (i % 2) == 0:
        # add value to list for even numbers
        even_numbers.append(i)
    # if value is odd
    elif (i % 2) != 0:
        # add value to list for odd numbers
        odd_numbers.append(i)
    # if value is equal to 0
    elif i == 0:
        # do nothing
        pass

# print list of odd numbers
print(f'Odd numbers:\n{odd_numbers}')
# print list of even numbers
print(f'Even numbers:\n{even_numbers}')

# if there is record in the list of odd numbers
if len(odd_numbers) != 0:
    # calculate and print AVG for odd numbers
    print(f'Odd numbers AVG: {sum(odd_numbers) / len(odd_numbers)}')
# if there are no records in the list
else:
    # print message
    print('No data to calculate')

# if there is record in the list of even numbers
if len(even_numbers) != 0:
    # calculate and print AVG for even numbers
    print(f'Even numbers AVG: {sum(even_numbers) / len(even_numbers)}')
# if there are no records in the list
else:
    # print message
    print('No Even numbers to calculate')
