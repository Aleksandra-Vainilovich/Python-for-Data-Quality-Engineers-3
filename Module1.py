
import random
from random import seed
from random import randint

#res = [random.randint(1, 1000) for i in range(100)]
res = [random.randrange(1, 1000) for i in range(100)]
print('List of random numbers ')
print(res)


for i in range(0, len(res)):
    for j in range(i + 1, len(res)):
        if res[i] > res[j]:
           res[i], res[j] = res[j], res[i]
print('List ordered:')
print(res)

Odd_numbers = []
Even_numbers = []
for x in res:
    if (x % 2) == 0:
        Even_numbers.append(x)
    else:
        Odd_numbers.append(x)

print('Odd numbers:')
print(Odd_numbers)
print('Even_numbers:')
print(Even_numbers)


def AVG_odd(Odd_numbers):
    if len(Odd_numbers) != 0:
        print(f'Odd_numbers SUM: {sum(Odd_numbers)/len(Odd_numbers)}')
    else:
        print('No data to calculate')


AVG_odd(Odd_numbers)


def AVG_even(Even_numbers):
    if len(Even_numbers) != 0:
        print(f'Even_numbers SUM: {sum(Even_numbers)/len(Even_numbers)}')
    else:
        print('No Even_numbers to calculate')


AVG_even(Even_numbers)

