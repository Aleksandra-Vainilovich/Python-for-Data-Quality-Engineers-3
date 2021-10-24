import os
import re

import datetime
import random

import Module4_task3

import json

import xml.etree.ElementTree as ET


class PrintMessage:
    def __init__(self, message):
        self.message = message

    def print_message(self):
        ptf = open("Module6.0.txt", "a")
        print(self.message, file=ptf)
        ptf.close()


class News:
    def __init__(self, news_msg, location):
        self.news_msg = news_msg
        self.location = location

    def news_message(self):
        message = f'News -------------------------\n{self.news_msg}\n{self.location}, {datetime.datetime.now().strftime("%d/%m/%y %H:%M")}\n\n'
        self.prt = PrintMessage(message)
        prt = self.prt
        prt.print_message()


class Advertising:
    def __init__(self, adv_message, actual_until=None):
        self.adv_message = adv_message
        self.actual_until = actual_until

    def advertising(self):
        message = f'Private Ad ------------------\n{self.adv_message}\nActual until: {self.actual_until}, {(datetime.datetime.strptime(self.actual_until, "%d/%m/%y") - datetime.datetime.now()).days} days left\n\n'
        self.prt = PrintMessage(message)
        prt = self.prt
        prt.print_message()


class WhoIs:
    def __init__(self, answer):
        self.answer = answer

    def ask_question(self):
        rand_num_list = [random.randrange(1, 100) for i in range(1)]
        question = f'How do you think? ----------\nWho killed Kennedy?\n{self.answer}\nprobability: {rand_num_list[0]} %\n\n'
        self.prt = PrintMessage(question)
        prt = self.prt
        prt.print_message()


class AddInfo:
    def __init__(self, source, target):
        self.source = source
        self.target = target

    def add_message(self):
        # Open source file to read
        open_source = open(self.source, 'r')
        # Open target file to appending to the end of the file
        open_target = open(self.target, 'a')
        # Write message from source file into target file
        for txt in open_source:
            open_target.write(txt)
        open_target.close()
        open_target = open(self.target, 'r')
        # If message was successfully written into target file, remove source file
        if txt in open_target:
            open_source.close()
            os.remove(self.source)
        else:
            open_source.close()
            print('File was not successfully processed')


class AddJson:
    def __init__(self, source, target):
        self.source = source
        self.target = target

    def parse_json(self):
        try:

            j_son = json.load(open(self.source))
            for i in j_son:

                if i['type'] == 'News -------------------------':
                    self.news = News(i['body'], i['location'])
                    news_mess = self.news
                    news_mess.news_message()
                    # variable for further source file text comparison
                    xml_news = i['body'] + i['location']

                elif i['type'] == 'Private ad ------------------':
                    self.advng = Advertising(i['body'], i['date'])
                    adv_message = self.advng
                    adv_message.advertising()
                    # variable for further source file text comparison
                    xml_ad = i['body'] + 'Actual until: ' + i['date']

                elif i['type'] == 'How do you think? ----------':
                    self.question = WhoIs(i['location'])
                    question_mess = self.question
                    question_mess.ask_question()
                    # variable for further source file text comparison
                    xml_ques = i['location']

                    try:
                        ptf = open(self.target)
                        lines = ptf.read()
                        # text from target file for further comparison
                        lines = lines.replace('\n', '').replace('\r', '').replace('\t', '')
                        ptf.close()

                        if xml_news in lines and xml_ad in lines and xml_ques in lines:
                            #open_source = open(self.target, 'r')
                            #open_source.close()
                            os.remove(self.source)
                    except:
                        print('Text was copied incorrectly. Import failed')

        except Exception as error:
            print(error)


class AddXml:
    def __init__(self, source, target):
        self.source = source
        self.target = target

    def parse_xml(self):
        try:

            xml_file = ET.parse(self.source)
            root = xml_file.getroot()
            for mes_type in root.iter():

                if mes_type.get('name') == 'News -------------------------':
                    self.news = News(mes_type.find("body").text, mes_type.find("location").text)
                    news_mess = self.news
                    news_mess.news_message()
                    # variable for further source file text comparison
                    xml_news = mes_type.get('name') + mes_type.find("body").text + mes_type.find("location").text

                elif mes_type.get('name') == 'Private Ad ------------------':
                    self.advng = Advertising(mes_type.find("body").text, mes_type.find("date").text)
                    adv_message = self.advng
                    adv_message.advertising()
                    # variable for further source file text comparison
                    xml_ad = mes_type.get('name') + mes_type.find("body").text + 'Actual until: ' + mes_type.find("date").text

                elif mes_type.get('name') == 'How do you think? ----------':
                    self.question = WhoIs(mes_type.find("body").text)
                    question_mess = self.question
                    question_mess.ask_question()
                    # variable for further source file text comparison
                    xml_ques = mes_type.get('name') + 'Who killed Kennedy?' + mes_type.find("body").text

                    try:
                        ptf = open(self.target)
                        lines = ptf.read()
                        # variable for further target file text comparison
                        lines = lines.replace('\n', '').replace('\r', '').replace('\t', '')
                        ptf.close()

                        if xml_news in lines and xml_ad in lines and xml_ques in lines:
                            os.remove(self.source)
                    except:
                        print('Text was copied incorrectly. Import failed')

        except Exception as error:
            print(error)


class Choice:
    def __init__(self, flag, target):
        self.flag = flag
        self.target = target

    def choose_message_type(self):
        if self.flag == '1':
            self.news = News(input('Please enter news text\n'), input('Please enter location\n'))
            news_mess = self.news
            news_mess.news_message()
        elif self.flag == '2':
            self.advng = Advertising(input('Please enter advertisment text\n'), input('Please enter expire date in the format dd/mm/yy\n'))
            adv_message = self.advng
            adv_message.advertising()
        elif self.flag == '3':
            self.question = WhoIs(input('Who killed Kennedy? Please enter your assumption\n'))
            question_mess = self.question
            question_mess.ask_question()
        elif self.flag == '4':
            self.copy_mess = AddInfo('Module6.0_paste.txt', self.target)
            copy_message = self.copy_mess
            copy_message.add_message()
        elif self.flag == '5':
            self.add_j_son = AddJson('test_mod8.json', self.target)
            add_json = self.add_j_son
            add_json.parse_json()
        elif self.flag == '6':
            self.add_xml = AddXml('Module9.xml', self.target)
            addxml = self.add_xml
            addxml.parse_xml()
        else:
            print('Your choice is not correct')

    def normalize(self):
        # Replace target words by spaces
        Module4_task3.findall_last_words = Module4_task3.findall_last_word(' ', '                ')
        # Send extra sentences, that are not ot be printed in target file, into variable
        remove_message = Module4_task3.new_sentence()

        # Open target file to read
        open_file = open(self.target, 'r')
        # Copy text from target file
        Module4_task3.initial_message = open_file.read()
        open_file.close()

        # Open target file for writing, truncating the file first
        open_file = open(self.target, 'w')
        # Apply normalization from Module4_task3.py with corresponding trigger
        normalized_text = Module4_task3.splitted('(\.\s+|\n)')
        # Remove extra sentences, that are not ot be printed in target file
        normalized_text = normalized_text.replace(remove_message, '', re.I)
        # Write final text into target file
        open_file.write(normalized_text)
        open_file.close()

make_your_choice = Choice(input('Please enter your choice:\n1 for News message\n2 for Advertisment\n3 for question of a day\n4 for copying existing messages from TXT file\n5 for existing JSON file data import\n6 for existing XML file data import\n'),
                       'Module6.0.txt')
make_your_choice.choose_message_type()
make_your_choice.normalize()



