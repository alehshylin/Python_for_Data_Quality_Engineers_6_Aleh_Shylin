# I import methods and classes from previous home tasks
from module_5_Classes_OOP import Classes_OOP as Classes
# In the 4 module I added new file with re-engineered method string_task() to make possible to call this functions and
# define text which will be transformed
from module_4_Functions import Functions_for_6_module as Functions
# Also import os method to work with file path
import os
# Shutil to copy files
import shutil
# And re to define input format of text in file
import re
# And datetime to compare dates in Adv news
from datetime import datetime
# Because file Module_Files remains the main, I import methods that count words and letters and use them in this file
from module_7_CSV import CSV as csv_module_7
# As file Module_Files remains the main, I import class from module 8 in this file
from module_8_JSON import JSON as json_module_8
# While Module_Files remains the main, I continue import classes to this file
from module_9_XML import XML as xml_module_9
# import method that insert rows to the sql table
from module_10_Database_Api import Database_Api as database_module_10


# All methods are in one class
class FileRecords:
    def __init__(self):
        self.backup_file_path = 'backup_directory/backup_file.txt'
        self.destination_path = os.path.abspath('file_directory')

    # This method copies file from default or user directory to the specific directory from which it will be parsed
    def file_actions_copy(self, file_path='backup_directory/backup_file.txt'):

        # If directory from which we will parse file is not exists, then we create it
        if not os.path.isdir(self.destination_path):
            os.mkdir(self.destination_path)

        # Split path
        file_path_list = os.path.split(file_path)
        # If file path is not default then I check, if this path exists or not
        if file_path != self.backup_file_path:
            folder_name = ''
            # Firstly I check if folder exists or not
            for i in range(len(file_path_list) - 1):
                folder_name = os.path.join(folder_name, file_path_list[i])
            if not os.path.isdir(folder_name):
                print('\nError: Such directory does not exist')
                return False
            else:
                # Then I check if file exists or not
                if not os.path.isfile(file_path):
                    print('\nError: Such file does not exist')
                    return False
        # I take full path
        file_path = os.path.abspath(file_path)
        # And try to copy file from path to the folder, from which I will parse text
        try:
            shutil.copy(file_path, self.destination_path)
        except IOError:
            print('\nError: Unable to copy such file')
            return False

    # This method parse text from file.
    def file_actions_parse(self):
        # Create list for text
        new_text_list = []
        # Just in case I create list with file names. In that case if there are two or more files, all files will be
        # processed
        file_names_list = os.listdir(self.destination_path)
        for file_name in file_names_list:
            file_path = os.path.join(self.destination_path, file_name)
            # We try to open file and take from it text
            try:
                with open(file_path, 'r', encoding="utf-8") as news_file:
                    text_from_file = news_file.read()
                    # I define records (news) are divided by '-' symbol which is repeated 3 or more times
                    text_from_file_list = re.split(r'-{3,}', text_from_file)
                    for text in text_from_file_list:
                        # I use strip() method to delete records that contain only whitespaces
                        text = text.strip()
                        text = text.lstrip('\n')
                        text = text.rstrip('\n')
                        # if text is string (i.e. not empty), then we...
                        if text:
                            # Call method from 4 module to transform record
                            text = Functions.string_task(text)
                            # And add transformed text to the list
                            new_text_list.append(text)
                # If parsing was performed correctly we delete file
                os.remove(file_path)
            # Otherwise we rise exception and end program
            except IOError:
                print('\n Error: Unable to parse a file')
                return False
        # If all files was correctly parsed, we return list with transformed text
        return new_text_list

    # This method add text to the Newsfeed according to the user choice. We can add text to the News or Adv headlines
    def text_actions_write(self, file_flag, text_file):

        csv_class = csv_module_7.CsvParsing()
        counter = 0
        for text in text_file:
            add_type = input(f"\nFor which Add you want to write this text: '{text}'? News or Adv?\n")
            add_type = add_type.lower()
            while add_type not in ('news', 'adv'):
                print(
                    f'You enter incorrect command - {add_type} - for Add choosing. Please, write News or Adv')
                add_type = input(f"\nFor which Add you want to write this text: '{text}'? News or Adv?\n")
                add_type = add_type.lower()
            if add_type == 'news':
                if counter == 1:
                    file_flag = 'no'
                city_text = Classes.NewsAdd().city_check()
                pointer = Classes.NewsAdd().message_module(file_flag, text, city_text)
                counter = 1
                # After one news was parsed, I call functions to count new words and letters
                csv_class.word_count()
                csv_class.letter_count()
                if pointer is False:
                    return False
            elif add_type == 'adv':
                if counter == 1:
                    file_flag = 'no'
                date_text = Classes.AdvAdd().date_module()
                if isinstance(date_text, bool):
                    return False
                while date_text <= datetime.today():
                    print(f"\nError: You entered date {date_text.strftime('%m/%d/%Y')} less or equal that today's "
                          f"date {datetime.today().strftime('%m/%d/%Y')}. Advertisement can be only with future dates.")
                    date_text = Classes.AdvAdd().date_module()
                    if isinstance(date_text, bool):
                        return False
                pointer = Classes.AdvAdd().message_module(file_flag, text, date_text)
                counter = 1
                # After one news was parsed, I call functions to count new words and letters
                csv_class.word_count()
                csv_class.letter_count()
                if pointer is False:
                    return False

    # This is the main menu of the module.
    def user_menu(self):

        file_records_class = FileRecords()
        oop_classes = Classes.UserChoose()
        csv_class = csv_module_7.CsvParsing()
        json_class = json_module_8.JSONRecords()
        xml_class = xml_module_9.XMLRecords()
        database_class = database_module_10.DatabaseAPI()

        # User can work with new module of with the module from homework 5
        text_flag = input('\nDo you want to write news by console of file? Console/File. Exit - end program\n')
        text_flag = oop_classes.user_menu_flag_checking(text_flag, ('console', 'file'))
        if text_flag == 'exit':
            return 'Program was ended by user'

        # We ask user if he wants to drop all tables from the database
        database_flag = input('\nDo you want to drop all tables from the database? Yes/No. Exit - end program\n')
        database_flag = oop_classes.user_menu_flag_checking(database_flag, ('yes', 'no'))
        if database_flag == 'exit':
            return 'Program was ended by user'
        # If user wants to drop tables then we drop them
        if database_flag == 'yes':
            database_class.table_drop()

        if text_flag == 'console':
            oop_classes.news_type_choice()
            # After user write news by console, I call functions to count new words and letters
            csv_class.word_count()
            csv_class.letter_count()

        elif text_flag == 'file':
            file_type_flag = input('\nDo you want to write news by .json, .txt or .xml? json/txt/xml. '
                                   'Exit - end program\n')
            file_type_flag = oop_classes.user_menu_flag_checking(file_type_flag, ('json', 'txt', 'xml'))
            if file_type_flag == 'exit':
                return 'Program was ended by user'

            file_flag = input('\nDo you want to re-write the file? Yes/No. Exit - end program\n')
            file_flag = oop_classes.user_menu_flag_checking(file_flag, ('yes', 'no'))
            if file_flag == 'exit':
                return 'Program was ended by user'

            directory_flag = input('\nDo you want to use default or new directory? Default/New. Exit - end program\n')
            directory_flag = oop_classes.user_menu_flag_checking(directory_flag, ('default', 'new'))
            if directory_flag == 'exit':
                return 'Program was ended by user'

            # If user select default directory we
            if directory_flag == 'default':
                if file_type_flag == 'txt':
                    # Call method that copies file from default folder
                    pointer = file_records_class.file_actions_copy()
                    # If pointer returns False, that means, that previous method fails, and we need to end the program
                    if pointer is False:
                        return False
                    # Parse this file
                    text_file = file_records_class.file_actions_parse()
                    if text_file is False:
                        return False
                    # And ask user to define, for which type of Newsfeed user wants to add record
                    file_records_class.text_actions_write(file_flag, text_file)
                elif file_type_flag == 'json':
                    pointer = json_class.json_actions_copy()
                    if pointer is False:
                        return False
                    text_file = json_class.json_actions_parse()
                    if text_file is False:
                        return False
                    pointer = json_class.text_json_actions_write(file_flag, text_file)
                    if pointer is False:
                        return False
                elif file_type_flag == 'xml':
                    pointer = xml_class.xml_actions_copy()
                    if pointer is False:
                        return False
                    xml_file = xml_class.xml_actions_parse()
                    if xml_file is False:
                        return False
                    xml_class.text_xml_actions_write(file_flag, xml_file)
            # If user select his/her directory
            elif directory_flag == 'new':
                if file_type_flag == 'txt':
                    # We ask user to write directory path (note: path should be absolute)
                    directory_path = input('\nPlease, enter your file path: \n')
                    # And perform the same steps as in the 'default path' way
                    pointer = FileRecords.file_actions_copy(self, file_path=directory_path)
                    if pointer is False:
                        return False
                    text_file = FileRecords.file_actions_parse(self)
                    if text_file is False:
                        return False
                    file_records_class.text_actions_write(file_flag, text_file)
                elif file_type_flag == 'json':
                    directory_path = input('\nPlease, enter your file path: \n')
                    pointer = json_class.json_actions_copy(file_path=directory_path)
                    if pointer is False:
                        return False
                    text_file = json_class.json_actions_parse()
                    if text_file is False:
                        return False
                    pointer = json_class.text_json_actions_write(file_flag, text_file)
                    if pointer is False:
                        return False
                elif file_type_flag == 'xml':
                    directory_path = input('\nPlease, enter your file path: \n')
                    pointer = xml_class.xml_actions_copy(file_path=directory_path)
                    if pointer is False:
                        return False
                    xml_file = xml_class.xml_actions_parse()
                    if xml_file is False:
                        return False
                    xml_class.text_xml_actions_write(file_flag, xml_file)

        # I select data from all tables in the end of the program
        print("\nBelow you can select table from which you want to select data")
        db_choose_flag = 'yes'
        while db_choose_flag == 'yes':
            db_flag = input('\nAvailable tables: news, adv, uniq. Exit - exit program\n')
            db_flag = oop_classes.user_menu_flag_checking(db_flag, ('news', 'adv', 'uniq'))
            if db_flag == 'news':
                database_class.table_select('news')
            elif db_flag == 'adv':
                database_class.table_select('adv')
            elif db_flag == 'uniq':
                database_class.table_select('uniq')
            elif db_flag == 'exit':
                return False
            else:
                print('Error: incorrect flag name')
                return False
            db_choose_flag = input('\nDo you want to select from another tables? yes/no:')
            db_choose_flag = oop_classes.user_menu_flag_checking(db_choose_flag, ('yes', 'no'))


if __name__ == "__main__":
    FileRecords().user_menu()
