import datetime
import random

class PrintMessage:
    def __init__(self, message):
        self.message = message

    def print_message(self):
        ptf = open("Info.txt", "a")
        print(self.message, file=ptf)
        ptf.close()


class News:
    def __init__(self, news_msg, location):
        self.news_msg = news_msg
        self.location = location

    def news_message(self):
        message = f'News -------------------------\n{self.news_msg}\n{self.location}, {datetime.datetime.now()}\n\n'
        self.prt = PrintMessage(message)
        prt = self.prt
        prt.print_message()

class Advertising:
    def __init__(self, adv_message, location, actual_until=None):
        self.adv_message = adv_message
        self.location = location
        self.actual_until = actual_until

    def advertising(self):
        message = f'News -------------------------\n{self.adv_message}\n{self.location}, {self.actual_until} , {(datetime.datetime.strptime(self.actual_until, "%m/%d/%y") - datetime.datetime.now()).days}\n\n'
        self.prt = PrintMessage(message)
        prt = self.prt
        prt.print_message()


class WhoIs:
    def __init__(self, answer):
        self.answer = answer

    def ask_question(self):
        rand_num_list = [random.randrange(1, 100) for i in range(1)]
        question = f'Who killed Kennedy?\n{self.answer}\nprobability: {rand_num_list[0]} %\n\n'
        self.prt = PrintMessage(question)
        prt = self.prt
        prt.print_message()


class Choice:
    def __init__(self, flag):
        self.flag = flag

    def choose_message_type(self):
        if self.flag == '1':
            self.news = News(input('Please enter news text\n'), input('Please enter location\n'))
            news_mess = self.news
            news_mess.news_message()
        elif self.flag == '2':
            self.advng = Advertising(input('Please enter advertisment text\n'), input('Please enter location\n'),
                                     input('Please enter due date in the format mm/dd/yy\n'))
            adv_message = self.advng
            adv_message.advertising()
        elif self.flag == '3':
            self.question = WhoIs(input('Please enter your assumption\n'))
            question_mess = self.question
            question_mess.ask_question()
        else:
            print('Your choice is not correct')


make_your_choice = Choice(input('Please enter your choice\n'))
make_your_choice.choose_message_type()
