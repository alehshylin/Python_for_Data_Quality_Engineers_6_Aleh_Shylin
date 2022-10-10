from module_5_Classes_OOP import Classes_OOP
from module_4_Functions import Functions
import os
import shutil


class FileRecords:
    def __init__(self):
        self.backup_file_path = 'backup_directory/backup_file.txt'
        self.destination_path = os.path.abspath('file_directory')

    def file_actions(self, file_path='backup_directory/backup_file.txt', delimiter='/'):

        if delimiter == '/':
            file_path_list = file_path.split('/')
        else:
            file_path_list = file_path.split('\\')

        if file_path != self.backup_file_path:
            folder_name = ''
            for i in range(len(file_path_list) - 1):
                folder_name += file_path_list[i] + delimiter
            if not os.path.isdir(folder_name):
                return -1
            else:
                if not os.path.isfile(file_path):
                    return -2

        file_path = os.path.abspath(file_path)

        try:
            shutil.copy(file_path, self.destination_path)
        except:
            pass

    def user_menu(self):
        pass


FileRecords().file_actions()
