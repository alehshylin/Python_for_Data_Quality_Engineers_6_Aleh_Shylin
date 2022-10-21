# import default packages for working
import os
import shutil
import json
from datetime import datetime
# import function to transform text
from module_4_Functions import Functions_for_6_module as Functions
# import classes to work with dates
from module_5_Classes_OOP import Classes_OOP as Classes
# import methods that count letters and words
from module_7_CSV import CSV as csv_module_7


# This class was imported to the file Module_Files. To work with class JSONRecords you need to execute file
# Module_Files.py
class JSONRecords:
    def __init__(self):
        self.backup_file_path = 'json_backup_directory/backup_json_file.json'
        self.destination_path = os.path.abspath('file_directory')

    # this method copies file from directories to target one
    def json_actions_copy(self, file_path='json_backup_directory/backup_json_file.json'):

        # if target directory doesn't exist we create it
        if not os.path.isdir(self.destination_path):
            os.mkdir(self.destination_path)

        # logic the same as in the method FileRecords.file_actions_copy() from module 6
        file_path_list = os.path.split(file_path)
        if file_path != self.backup_file_path:
            folder_name = ''
            for i in range(len(file_path_list) - 1):
                folder_name = os.path.join(folder_name, file_path_list[i])
            if not os.path.isdir(folder_name):
                print('\nError: Such directory does not exist')
                return False
            else:
                if not os.path.isfile(file_path):
                    print('\nError: Such file does not exist')
                    return False
        file_path = os.path.abspath(file_path)
        try:
            shutil.copy(file_path, self.destination_path)
        except IOError:
            print('\nError: Unable to copy such file')
            return False

    # this method parse json from file to variable
    def json_actions_parse(self):
        file_names_list = os.listdir(self.destination_path)
        for file_name in file_names_list:
            file_path = os.path.join(self.destination_path, file_name)
            # we try to load data
            try:
                json_data = json.load(open(file_path))
                # if we succeed load data we delete file
                os.remove(file_path)
                # and return variable with json
                return json_data
            # if we can't open file
            except IOError:
                # we raise exception
                print('\n Error: Unable to parse a file')
                # and exit the program
                return False

    # this method works with json from variable. It defines from which news type should go text and transform it if
    # necessary
    def text_json_actions_write(self, file_flag, json_file):

        # create sets for keys checking
        set_for_news = {'news_text', 'news_city'}
        set_for_adv = {'adv_text', 'adv_date'}
        counter = 0
        # if key in json
        if 'newsfeed' in json_file:
            # for each dict in the list
            for news_dict in json_file['newsfeed']:
                # if key in the dict
                if 'news_type' in news_dict:
                    if news_dict['news_type'].lower() == 'news':
                        # if dict contains keys from set
                        if set_for_news.issubset(news_dict):
                            # we transform text
                            news_dict['news_text'] = Functions.string_task(news_dict['news_text'])
                            if counter == 1:
                                file_flag = 'no'
                            # and write text and city to the newsfeed file
                            pointer = Classes.NewsAdd().message_module(file_flag, news_dict['news_text'],
                                                                       news_dict['news_city'])
                            counter = 1
                            csv_module_7.CsvParsing().word_count()
                            csv_module_7.CsvParsing().letter_count()
                            if pointer is False:
                                return False
                        # if dict doesn't contain keys we raise an error
                        else:
                            print("Error: incorrect json format")
                            return False
                    # same for 'adv' type
                    elif news_dict['news_type'].lower() == 'adv':
                        if set_for_adv.issubset(news_dict):
                            news_dict['adv_text'] = Functions.string_task(news_dict['adv_text'])
                            if counter == 1:
                                file_flag = 'no'
                            # But here we also work with date. If date from json is not correct we ask user to write
                            # new date
                            try:
                                news_dict['adv_date'] = datetime.strptime(news_dict['adv_date'], '%m/%d/%Y')
                            except (ValueError, TypeError):
                                print("\nError: Incorrect data format. We will ask you to write new date")
                                news_dict['adv_date'] = Classes.AdvAdd().date_module()
                            while news_dict['adv_date'] <= datetime.today():
                                print(
                                    f"\nError: You entered date {news_dict['adv_date'].strftime('%m/%d/%Y')} "
                                    f"less or equal that today's date {datetime.today().strftime('%m/%d/%Y')}. "
                                    f"Advertisement can be only with future dates.")
                                news_dict['adv_date'] = Classes.AdvAdd().date_module()
                            pointer = Classes.AdvAdd().message_module(file_flag, news_dict['adv_text'],
                                                                      news_dict['adv_date'])
                            csv_module_7.CsvParsing().word_count()
                            csv_module_7.CsvParsing().letter_count()
                            if pointer is False:
                                return False
                        # if dict doesn't contain keys we raise an error
                        else:
                            print("\nError: incorrect json format")
                            return False
                    # if dict doesn't have correct value for 'news_type' key we raise an error
                    else:
                        print("\nError: incorrect value for 'news_type' key")
                        return False
                # if dict doesn't contain key we raise an error
                else:
                    print("\nError: incorrect json format")
                    return False
        # if dict doesn't contain key we raise an error
        else:
            print("\nError: incorrect json format")
            return False


if __name__ == '__main__':
    JSONRecords().json_actions_copy()
    a = JSONRecords().json_actions_parse()
    print(a)
