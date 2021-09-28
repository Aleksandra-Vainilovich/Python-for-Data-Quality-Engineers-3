import random
import string

# Return and print c randomly selected integer values from a to b
def random_number_list(a, b, c):
    return [random.randrange(a, b) for i in range(c)]


def random_dictionary(a):
    global random_dictionary
    for z in random_number_list:
        random_dictionary = [{str(j): random.randrange(1, 100) for z in range(1) for j in random.choices(string.ascii_lowercase, k= random_number_list[a])}
          , {str(j): random.randrange(1, 100) for z in range(1) for j in random.choices(string.ascii_lowercase, k= random_number_list[a])}]
        return random_dictionary


def updated_dictionary():
    updated_dict = {}
    for dictionary in random_dictionary:
        updated_dict = random_dictionary[1]
        for key, value in random_dictionary[0].items():
            if key in updated_dict:
                if updated_dict[key] > value:
                    key_updated, updated_dict[key_updated] = f'{key}_2', updated_dict[key]
                    key_updated = updated_dict.pop(key)
                else:
                    key_updated, updated_dict[key_updated] = f'{key}_1', value
                    key_updated = updated_dict.pop(key)
            else:
                updated_dict[key] = value
            if key in updated_dict:
                updated_dict[key] = updated_dict.pop(key)
        return f'Updated dictionary:\n{updated_dict}'


# Enter c integer values from a to b: (a, b, c)
random_number_list = random_number_list(1, 26, 26)
print(random_number_list)

# enter random number to set dictionary length
random_dictionary(3)
print(f'Random dictionary:\n{random_dictionary}')

print(updated_dictionary())


