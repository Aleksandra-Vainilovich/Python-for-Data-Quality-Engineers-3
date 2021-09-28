# import module re
import re


# Last words of each existing sentence
def findall_last_word(a, b):
    return re.findall(a, b)


# One more sentence with last words of each existing sentence
def new_sentence():
    variable = findall_last_word[0]
    view = findall_last_word[1]
    paragraph = findall_last_word[2]
    here = findall_last_word[3]
    mistake = findall_last_word[4]
    text = findall_last_word[5]
    whitespaces = findall_last_word[6]
    nbr = findall_last_word[7]
    return f'\n\n\t{here} is a {mistake} in {text} {paragraph}. To my {view} {variable} should have more than {nbr} {whitespaces}.\n'


def splitted(a):
    # Add new sentence to the end of this paragraph
    message = initial_message + new_sentence()
    # split message on pattern
    splitted = re.split(a, message)
    # capitalize first letter or sentences
    capital_letters = [i.capitalize() for i in splitted]
    # join all parts back
    return ''.join(capital_letters)


# Replace iz by is if necessary
def misspelling(a, b):
    return splitted.replace(a, b)


# Calculate number of whitespace characters in this text
def filtered_whitesp():
    return len(list(s for s in misspelling if s.isspace()))


# Text variable
initial_message = """tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""


findall_last_word = findall_last_word('\s(\w+)?\.', initial_message)
#print(findall_last_word)

splitted = splitted('(\.\s+)')

misspelling = misspelling(" iz", " is")
print(f'Corrected mistakes:\n{misspelling}')


print(f'Number of whitespaces: {filtered_whitesp()}')



