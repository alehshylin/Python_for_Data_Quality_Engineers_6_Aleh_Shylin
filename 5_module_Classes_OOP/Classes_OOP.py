from pathlib import Path
from datetime import datetime


class NewsAdd:
    def __init__(self):
        self.add_type = 'News'
        self.filename = 'Newsfeed.txt'
        self.filepath = Path(self.filename)

    def file_module(self, file_flag='0', text_message='Text message', text_city='Vilnius'):
        if self.filepath.is_file():
            if file_flag == '1':
                with open(self.filename, 'w') as NewsFile:
                    file_text = ['News ------------------------------\n', f'{text_message} \n',
                                 f"{text_city}, {datetime.now().strftime('%m/%d/%Y %H.%M')} \n"
                        , '-----------------------------------\n\n']
                    NewsFile.writelines(file_text)
            elif file_flag == '0':
                with open(self.filename, 'a') as NewsFile:
                    file_text = ['News ------------------------------\n', f'{text_message} \n',
                                 f"{text_city}, {datetime.now().strftime('%m/%d/%Y %H.%M')} \n"
                        , '-----------------------------------\n\n']
                    NewsFile.writelines(file_text)
        else:
            with open(self.filename, 'w') as NewsFile:
                file_text = ['News ------------------------------\n', f'{text_message} \n',
                             f"{text_city}, {datetime.now().strftime('%m/%d/%Y %H.%M')} \n"
                    , '-----------------------------------\n\n']
                NewsFile.writelines(file_text)

    def user_message(self, file_flag):
        news_text = input('Please, write your News: ')
        city_text = input('Please, write your City: ')
        NewsAdd.file_module(file_flag, news_text, city_text)


class AdvAdd(NewsAdd):
    def __init__(self):
        NewsAdd.__init__(self)
        self.add_type = 'Adv'

    def file_module(self, file_flag='0', text_message='Text message',
                    text_exp_date=datetime(2022, 12, 31)):
        if self.filepath.is_file():
            if file_flag == '1':
                with open(self.filename, 'w') as NewsFile:
                    file_text = ['Private ad ------------------------\n', f'{text_message} \n',
                                 f"Actual until {text_exp_date.strftime('%m/%d/%Y')}, "
                                 f"{abs((text_exp_date - datetime.now()).days)} days left \n"
                                 , '-----------------------------------\n\n']
                    NewsFile.writelines(file_text)
            elif file_flag == '0':
                with open(self.filename, 'a') as NewsFile:
                    file_text = ['Private ad ------------------------\n', f'{text_message} \n',
                                 f"Actual until {text_exp_date.strftime('%m/%d/%Y')}, "
                                 f"{abs((text_exp_date - datetime.now()).days)} days left \n"
                                 , '-----------------------------------\n\n']
                    NewsFile.writelines(file_text)
        else:
            with open(self.filename, 'w') as NewsFile:
                file_text = ['Private ad ------------------------\n', f'{text_message} \n',
                             f"Actual until {text_exp_date.strftime('%m/%d/%Y')}, "
                             f"{abs((text_exp_date - datetime.today()).days)} days left \n"
                             , '-----------------------------------\n\n']
                NewsFile.writelines(file_text)

    def user_message(self, file_flag):
        adv_text = input('Please, write your Advertisement: ')
        date_text = input('Please, write date, until your advertisement is active in format MM/DD/YYYY: ')

        NewsAdd.file_module(file_flag, adv_text, date_text)



class UniqueAdd(NewsAdd):
    pass


class UserChoose:

    def news_type_choose(self):
        file_flag = input('Do you want to re-write the file? Yes/No. Exit - end program')
        file_flag.lower()
        file_flag.capitalize()

        if file_flag == 'Exit':
            return 'Program was ended by user'

        while (file_flag != 'Yes') or (file_flag != 'No'):
            print(f'You enter incorrect command - {file_flag} - for file re-writing. Please, write Yes or No')
            file_flag = input('Do you want to re-write the file? Yes/No Exit - end program')
            file_flag.lower()
            file_flag.capitalize()
            if file_flag == 'Exit':
                return 'Program was ended by user'

        add_type = input('What type of Add do you want to write? News/Adv/Unique. Exit - end program')
        add_type.lower()
        add_type.capitalize()

        if add_type == 'Exit':
            return 'Program was ended by user'

        while (add_type != 'News') or (add_type != 'Adv') or (add_type != 'Unique'):
            print(f'You enter incorrect command - {add_type} - for Add choosing. Please, write News or Adv or Unique')
            add_type = input('What type of Add do you want to write? News/Adv/Unique. Exit - end program')
            add_type.lower()
            add_type.capitalize()
            if add_type == 'Exit':
                return 'Program was ended by user'

        if add_type == 'News':
            NewsAdd.user_message(NewsAdd(), file_flag)
        elif add_type == 'Adv':
            pass
        elif add_type == 'Unique':
            pass
