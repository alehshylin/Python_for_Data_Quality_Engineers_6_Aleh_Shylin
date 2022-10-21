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
                with open(file_path, 'r') as news_file:
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
                csv_module_7.CsvParsing().word_count()
                csv_module_7.CsvParsing().letter_count()
                if pointer is False:
                    return False
            elif add_type == 'adv':
                if counter == 1:
                    file_flag = 'no'
                date_text = Classes.AdvAdd().date_module()
                while date_text <= datetime.today():
                    print(f"\nError: You entered date {date_text.strftime('%m/%d/%Y')} less or equal that today's "
                          f"date {datetime.today().strftime('%m/%d/%Y')}. Advertisement can be only with future dates.")
                    date_text = Classes.AdvAdd().date_module()
                pointer = Classes.AdvAdd().message_module(file_flag, text, date_text)
                counter = 1
                # After one news was parsed, I call functions to count new words and letters
                csv_module_7.CsvParsing().word_count()
                csv_module_7.CsvParsing().letter_count()
                if pointer is False:
                    return False

    # This is the main menu of the module.
    def user_menu(self):
        # User can work with new module of with the module from homework 5
        text_flag = input('\nDo you want to write news by console of file? Console/File. Exit - end program\n')
        text_flag = text_flag.lower()

        if text_flag == 'exit':
            print('\nProgram was ended by user')
            return 'Program was ended by user'

        while text_flag not in ('console', 'file'):
            print(f'\nYou enter incorrect command - {text_flag} - for news writing. Please, write Console or File')
            text_flag = input('\nDo you want to write news by console of file? Console/File.\n')
            text_flag = text_flag.lower()
            if text_flag == 'exit':
                print('\nProgram was ended by user')
                return 'Program was ended by user'

        if text_flag == 'console':
            Classes.UserChoose().news_type_choice()
            # After user write news by console, I call functions to count new words and letters
            csv_module_7.CsvParsing().word_count()
            csv_module_7.CsvParsing().letter_count()
        elif text_flag == 'file':
            file_flag = input('\nDo you want to re-write the file? Yes/No. Exit - end program\n')
            file_flag = file_flag.lower()

            if file_flag == 'exit':
                print('\nProgram was ended by user')
                return 'Program was ended by user'

            # Logic of the menu is almost the same as in the 5 homework
            while file_flag not in ('yes', 'no'):
                print(f'You enter incorrect command - {file_flag} - for file re-writing. Please, write Yes or No')
                file_flag = input('Do you want to re-write the file? Yes/No. Exit - end program\n')
                file_flag = file_flag.lower()
                if file_flag == 'exit':
                    print('\nProgram was ended by user')
                    return 'Program was ended by user'

            directory_flag = input('\nDo you want to use default or new directory? Default/New. Exit - end program\n')
            directory_flag = directory_flag.lower()
            if directory_flag == 'exit':
                print('\nProgram was ended by user')
                return 'Program was ended by user'

            while directory_flag not in ('default', 'new'):
                print(f'\nYou wrote incorrect command {directory_flag}. Please, enter Default or New')
                directory_flag = input('\nDo you want to use default or new directory? Default/New. Exit - end '
                                       'program\n')
                directory_flag = directory_flag.lower()
                if directory_flag == 'exit':
                    print('\nProgram was ended by user')
                    return 'Program was ended by user'

            # If user select default directory we
            if directory_flag == 'default':
                # Call method that copies file from default folder
                pointer = FileRecords.file_actions_copy(self)
                # If pointer returns False, that means, that previous method fails, and we need to end the program
                if pointer is False:
                    return False
                # Parse this file
                text_file = FileRecords.file_actions_parse(self)
                if text_file is False:
                    return False
                # And ask user to define, for which type of Newsfeed user wants to add record
                FileRecords().text_actions_write(file_flag, text_file)
            # If user select his/her directory
            elif directory_flag == 'new':
                # We ask user to write directory path (note: path should be absolute)
                directory_path = input('\nPlease, enter your file path: \n')
                # And perform the same steps as in the 'default path' way
                pointer = FileRecords.file_actions_copy(self, file_path=directory_path)
                if pointer is False:
                    return False
                text_file = FileRecords.file_actions_parse(self)
                if text_file is False:
                    return False
                FileRecords().text_actions_write(file_flag, text_file)


if __name__ == "__main__":
    FileRecords().user_menu()
