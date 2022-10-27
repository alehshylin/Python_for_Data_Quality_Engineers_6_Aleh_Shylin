# import default packages for working
import os
import shutil
from datetime import datetime
# import ElementTree package to work with xml files
import xml.etree.ElementTree as ET
# import function to transform text
from module_4_Functions import Functions_for_6_module as Functions
# import classes to work with dates
from module_5_Classes_OOP import Classes_OOP as Classes
# import methods that count letters and words
from module_7_CSV import CSV as csv_module_7

# This class was imported to the file Module_Files. To work with class XMLRecords you need to execute file
# Module_Files.py
class XMLRecords:

    def __init__(self):
        self.backup_file_path = 'xml_backup_directory/backup_xml_file.xml'
        self.destination_path = os.path.abspath('file_directory')

    # This method copies xml file from backup/user directory to main directory
    def xml_actions_copy(self, file_path='xml_backup_directory/backup_xml_file.xml'):

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

    # this method parse xml file from the main directory
    def xml_actions_parse(self):
        file_names_list = os.listdir(self.destination_path)
        for file_name in file_names_list:
            file_path = os.path.join(self.destination_path, file_name)
            # we try to load data
            try:
                # parse xml file to variable
                xml_file_parse = ET.parse(file_path)
                # get data from ElementTree object
                xml_file = xml_file_parse.getroot()
                # if we succeed load data we delete file
                os.remove(file_path)
                # and return variable with json
                return xml_file
            # if we can't open file
            except IOError:
                # we raise exception
                print('\n Error: Unable to parse a file')
                # and exit the program
                return False

    # this method write data from xml to the newsfeed file
    def text_xml_actions_write(self, file_flag, xml_file):
        # counter for news from xml file
        counter_for_all = 0
        # counter for news from xml file that will fail in writing
        counter_for_failed = 0
        # flag for file_flag variable. If file_flag variable == 'yes' then we overwrite file only first time. Later we
        # change this flag to the 'no'
        flag_counter = 0
        # read whole xml file
        for newsfeed in xml_file:
            # in this dict I parse each <news_feed> data
            xml_dict = {}
            counter_for_all += 1
            # if main tag name == 'news_feed'
            if 'news_feed' in newsfeed.tag:
                # for each tag in the <news_feed>
                for news in newsfeed:
                    # we add tag and value to the dict
                    xml_dict.update({news.tag: news.text})
                # if dict contains news_type
                if 'news_type' in xml_dict.keys():
                    # check news_type value
                    if xml_dict['news_type'].lower() == 'news':
                        # if dict contains necessary keys
                        if {'news_text', 'news_city'}.issubset(xml_dict.keys()):
                            # transform text
                            xml_dict['news_text'] = Functions.string_task(xml_dict['news_text'])
                            if flag_counter == 1:
                                file_flag = 'no'
                            # and write news to the newsfeed file
                            pointer = Classes.NewsAdd().message_module(file_flag, xml_dict['news_text'],
                                                                       xml_dict['news_city'])
                            flag_counter = 1
                            # count words in newsfeed file
                            csv_module_7.CsvParsing().word_count()
                            # count letters in newsfeed file
                            csv_module_7.CsvParsing().letter_count()
                            # if news wasn't written to the file, then we count it as failed news
                            if pointer is False:
                                counter_for_failed += 1
                        else:
                            # if dict doesn't contain necessary keys, then we count it as failed news
                            counter_for_failed += 1
                    # same logic for the advertisement
                    elif xml_dict['news_type'].lower() == 'adv':
                        if {'adv_text', 'adv_date'}.issubset(xml_dict.keys()):
                            xml_dict['adv_text'] = Functions.string_task(xml_dict['adv_text'])
                            if flag_counter == 1:
                                file_flag = 'no'
                            # if data format is not correct
                            try:
                                xml_dict['adv_date'] = datetime.strptime(xml_dict['adv_date'], '%m/%d/%Y')
                            # we raise an error and ask user to write new date
                            except (ValueError, TypeError):
                                print(f"\nError: Incorrect data format for adv: \n{xml_dict['adv_text']}.\n"
                                      f"We will ask you to write new date")
                                xml_dict['adv_date'] = Classes.AdvAdd().date_module()
                            # while date is less than today
                            while xml_dict['adv_date'] <= datetime.today():
                                # we ask user to write new date
                                print(
                                    f"\nError: You entered date {xml_dict['adv_date'].strftime('%m/%d/%Y')} "
                                    f"less or equal that today's date {datetime.today().strftime('%m/%d/%Y')}. "
                                    f"Advertisement can be only with future dates.")
                                xml_dict['adv_date'] = Classes.AdvAdd().date_module()
                            # after all we write adv to the newsfeed file
                            pointer = Classes.AdvAdd().message_module(file_flag, xml_dict['adv_text'],
                                                                       xml_dict['adv_date'])
                            flag_counter = 1
                            csv_module_7.CsvParsing().word_count()
                            csv_module_7.CsvParsing().letter_count()
                            if pointer is False:
                                counter_for_failed += 1
                        else:
                            # if dict doesn't contain necessary keys, then we count it as failed news
                            counter_for_failed += 1
                    else:
                        # if dict doesn't contain necessary keys, then we count it as failed news
                        counter_for_failed += 1
                else:
                    # if dict doesn't contain necessary keys, then we count it as failed news
                    counter_for_failed += 1
            else:
                # if tag name is not 'news_feed', then we count it as failed news
                counter_for_failed += 1

        # After all we print news processing info
        print(f'\nOverall news from .xml file: {counter_for_all}, failed news: {counter_for_failed}, '
              f'news that were written into the newsfeed file: {counter_for_all - counter_for_failed}')


if __name__ == '__main__':
    XMLRecords().xml_actions_copy()
    xml_file = XMLRecords().xml_actions_parse()
    XMLRecords().text_xml_actions_write('yes', xml_file)
