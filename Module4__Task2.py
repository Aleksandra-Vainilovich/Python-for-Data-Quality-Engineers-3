import random
import string

# Return and print 100 randomly selected integer values from 1 to 1000
def random_number_list(a, b, c):
    return [random.randrange(a, b) for i in range(c)]

random_number_list = random_number_list(1, 26, 26)


def random_dictionary(a):
    global random_dictionary
    for z in random_number_list:
        random_dictionary = [{str(j): random.randrange(1, 100) for z in range(1) for j in random.choices(string.ascii_lowercase, k= random_number_list[a])}
          , {str(j): random.randrange(1, 100) for z in range(1) for j in random.choices(string.ascii_lowercase, k= random_number_list[a])}]
    return random_dictionary


random_dictionary = random_dictionary(3)
random_dict = random_dictionary.copy()
print(f'Random dictionary:\n{random_dict}')


def updated_dictionary():
    updated_dict = {}
    for dictionary in random_dict:
        updated_dict = random_dict[1]
        for key, value in random_dict[0].items():
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
        return updated_dict


print(f'upd:\n{updated_dictionary()}')

