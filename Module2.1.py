import random
import string

# Return and print 100 randomly selected integer values from 1 to 1000
rand_num_list = [random.randrange(1, 26) for i in range(26)]

# select single integer value from random list created
for i in rand_num_list:
    rand_num = rand_num_list[3]

# create list of two (should be random) dictionaries with random number of items
mydict = [{str(j): random.randrange(1, 100) for i in range(1) for j in random.choices(string.ascii_lowercase, k= rand_num)}
          , {str(j): random.randrange(1, 100) for i in range(1) for j in random.choices(string.ascii_lowercase, k= rand_num)}]

print(f'Random dictionary:\n{mydict}')

# create separate dictionary from the second dictionary of mydict
updated_dict = {}
for dictionary in mydict:
    print(f'dictionary:\n{dictionary}')
    updated_dict = mydict[1]

# for all key-value pairs in first element of mydict
for key, value in mydict[0].items():
    # if key is listed in the copy of the second element of mydict
    if key in updated_dict:
        # if value in the second element of the mydict is bigger than value in the first element of the mydict
        # with the similar key names
        if updated_dict[key] > value:
            # create new key with new name and bigger value
            key_updated, updated_dict[key_updated] = f'{key}_2', updated_dict[key]
            # exclude old name of the element from updated_dict
            key_updated = updated_dict.pop(key)
        else:
            key_updated, updated_dict[key_updated] = f'{key}_1', value
            key_updated = updated_dict.pop(key)
    else:
        # add key-value pairs from the the first element of mydict to updated_dict
        updated_dict[key] = value

    if key in updated_dict:
        # exclude key-value pairs with keys listed both in the first element of mydict and updated_dict
        updated_dict[key] = updated_dict.pop(key)

print(f'Updated dictionary with new keys:\n{updated_dict}')
