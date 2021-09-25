# import modules re, string
import re
import string

# Text variable
initial_message = """tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

# Last words of each existing sentence
findall_last_word = re.findall(r'\s(\w+)?\.', initial_message)

variable = findall_last_word[0]
view = findall_last_word[1]
paragraph = findall_last_word[2]
here = findall_last_word[3]
mistake = findall_last_word[4]
text = findall_last_word[5]
whitespaces = findall_last_word[6]
nbr = findall_last_word[7]

# One more sentence with last words of each existing sentence
new_sentence = f'\n\n\t{here} is a {mistake} in {text} {paragraph}. To my {view} {variable} should have more than {87} {whitespaces}.\n'

# Adding new sentence to the end of this paragraph
message = initial_message + new_sentence

# split message
normalized = re.split('(\.\s+)', message)

# Capitalize irst letters of each sentence
capital_letters = [i.capitalize() for i in normalized]

# Union back into single message
capitalized_message = ''.join(capital_letters)

# Replacing iz by is in necessary
misspelling = capitalized_message.replace(' iz', ' is')
print(f'Corrected mistakes:\n{misspelling}')

# Calculate number of whitespace characters in this text
filtered_whitesp = list(s for s in misspelling if s.isspace())
print(f'Number of whitespaces: {len(filtered_whitesp)}')

