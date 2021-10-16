import csv
import re


class WordCount:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def write_to_csv(self):
        with open(self.input_file, 'r') as read_txt:
            data_to_read = read_txt.read()
            row = data_to_read.lower()
            list_with_numbers = re.findall(r'\w+', row)
            output_list = [x for x in list_with_numbers if not any(i.isdigit() for i in x)]
            read_txt.close()

        count_dict = {}
        for i in output_list:
            count_dict[i] = output_list.count(i)
            read_txt.close()

        with open(self.output_file, 'w', encoding='UTF8', newline='') as csvfile:
            for key, value in count_dict.items():
                writer = csv.writer(csvfile, delimiter='-')
                writer.writerow([key, output_list.count(key)])
            csvfile.close()


word_count = WordCount("Module6.0.txt", 'Module7.csv')
word_count.write_to_csv()


class LettersCount:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def write_to_csv(self):
        with open(self.input_file, 'r') as read_txt:
            data_to_read = read_txt.read()
            row = data_to_read.lower()
            # lists of words with letters in lowercase/initial
            list_with_numbers = re.findall(r'\w+', row)
            list_with_numbers_init = re.findall(r'\w+', data_to_read)
            # lists of words with letters in lowercase/initial excluding numbers
            output_list = [x for x in list_with_numbers if not any(i.isdigit() for i in x)]
            output_list_init = [x for x in list_with_numbers_init if not any(i.isdigit() for i in x)]
            # strings of united words
            string_united = ''.join(output_list)
            string_united_init = ''.join(output_list_init)
            # lists of letters in lowercase/initial
            string_united = list(string_united)
            string_united_init = list(string_united_init)
            # list of letters in uppercase
            string_united_init = list(''.join([x for x in string_united_init if x.isupper()]))

            count_dict = {}
            for i in string_united:
                count_dict[i] = string_united.count(i)
            count_dict_upper = {}
            for x in string_united_init:
                count_dict_upper[x] = string_united_init.count(x)
            read_txt.close()

        with open(self.output_file, 'w', encoding='UTF8', newline='') as csvfile:
            headers = ['letter', 'count_all', 'count_uppercase', 'percentage']
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            # count number of letters
            count_letters = len(string_united)
            for key, value in count_dict.items():
                writer = csv.writer(csvfile, delimiter=',')
                writer.writerow([key, string_united.count(key), '', round(string_united.count(key)/count_letters*100, 2)])
            for key, value in count_dict_upper.items():
                writer = csv.writer(csvfile, delimiter=',')
                writer.writerow([key, '', string_united_init.count(key), round(string_united_init.count(key)/count_letters*100, 2)])
            csvfile.close()

letters_count = LettersCount("Module6.0.txt", 'Module7.2.csv')
letters_count.write_to_csv()
