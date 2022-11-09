# import pyodbc to work with the databases
import pyodbc


class DatabaseAPI:

    def __init__(self):
        # in the init I create connection to the database
        with pyodbc.connect('Driver=SQLite3 ODBC Driver;Database=sqlite.db') as self.connection:
            # and create cursor that will be auto-closed in the end of the program
            with self.connection.cursor() as self.cursor:
                pass

    # This function writes rows into tables and creates table if it doesn't exist
    def table_write(self, table_name, value_1, value_2):

        # replace \n to spaces for all values in the row, because row contains data in one line
        value_1 = value_1.replace('\n', ' ')
        value_2 = value_2.replace('\n', ' ')

        # I have three tables for three types of news
        if table_name == 'news':
            # If table doesn't exists we create it
            self.cursor.execute(
                f"CREATE TABLE IF NOT EXISTS {table_name} (news_text varchar(512), news_city varchar(64))")
            # duplicate check
            self.cursor.execute(f"SELECT COUNT(*) FROM {table_name} WHERE news_text='{value_1}' "
                                f"AND news_city='{value_2}'")
            result = self.cursor.fetchall()
            # if there is a duplicate
            if result[0][0] != 0:
                # I raise an error
                print(f"\n\nMessage from the database! "
                      f"\nRow with values: \n{value_1}; {value_2} \nIs already exists in the table: {table_name}")
            else:
                # otherwise I insert row into the table
                self.cursor.execute(f"INSERT INTO {table_name} VALUES ('{value_1}', '{value_2}')")
            # after all operations I commit transactions
            self.cursor.commit()

        # same logic applies for all tables
        elif table_name == 'adv':
            self.cursor.execute(
                f"CREATE TABLE IF NOT EXISTS {table_name} (adv_text varchar(512), adv_date varchar(32))")
            self.cursor.execute(f"SELECT COUNT(*) FROM {table_name} WHERE adv_text='{value_1}' "
                                f"AND adv_date='{value_2}'")
            result = self.cursor.fetchall()
            if result[0][0] != 0:
                print(f"\n\nMessage from the database! "
                      f"\nRow with values: \n{value_1}; {value_2} \nIs already exists in the table: {table_name}")
            else:
                self.cursor.execute(f"INSERT INTO {table_name} VALUES ('{value_1}', '{value_2}')")
            self.cursor.commit()

        elif table_name == 'uniq':
            self.cursor.execute(
                f"CREATE TABLE IF NOT EXISTS {table_name} (city_text varchar(64), zodiac_sign varchar(64))")
            self.cursor.execute(f"SELECT COUNT(*) FROM {table_name} WHERE city_text='{value_1}' "
                                f"AND zodiac_sign='{value_2}'")
            result = self.cursor.fetchall()
            if result[0][0] != 0:
                print(f"\n\nMessage from the database! "
                      f"\nRow with values: \n{value_1}; {value_2} \nIs already exists in the table: {table_name}")
            else:
                self.cursor.execute(f"INSERT INTO {table_name} VALUES ('{value_1}', '{value_2}')")
            self.cursor.commit()
        # If table_name is not correct, I raise self-made error
        else:
            print(f'\nError: incorrect table name {table_name}')
            return False

    # This function select all rows from specific table
    def table_select(self, table_name):

        try:
            # try to select result
            self.cursor.execute(f"SELECT * FROM {table_name}")
            result = self.cursor.fetchall()
            print(f"\nRows in the table {table_name}: ")
            for row in result:
                print(row)
        except pyodbc.Error:
            # if select statement failed I raise self-made error
            print(f"\nError: table {table_name} does not exists in the database.")

    # This function drop all tables in one time
    def table_drop(self):
        # select table names from meta tables
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%'")
        table_names_list = self.cursor.fetchall()
        for table_tuple in table_names_list:
            for table_name in table_tuple:
                try:
                    # And try to drop it
                    self.cursor.execute(f"DROP TABLE {table_name}")
                    print(f"\nTable {table_name} was deleted successfully")
                except pyodbc.Error:
                    # If I can't drop, I raise an error
                    print(f"\nError: table {table_name} wasn't deleted")
        # after all operations I commit transactions
        self.cursor.commit()


if __name__ == '__main__':
    DatabaseAPI().table_write('news', 'asd', 'dsa')
    DatabaseAPI().table_write('adv', 'asd', 'dsa')
    DatabaseAPI().table_write('uniq', 'asd', 'dsa')
    DatabaseAPI().table_select('news')
    DatabaseAPI().table_select('adv')
    DatabaseAPI().table_select('uniq')
    DatabaseAPI().table_drop()

