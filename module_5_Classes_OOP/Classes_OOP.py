# I import Path method from pathlib module to work with file's path
from pathlib import Path
# I import datetime method from datetime to work with date (take now datetime, convert date, i.e.)
from datetime import datetime
# I import sleep to pause program when I try to reach API or file
from time import sleep
# I import requests module to work with API (I use API in my own class)
import requests
# I import geopy.geocoders module to use it in my own class. As overall: this is an API that gives you information
# about the street or city or country. More info you can find here https://geopy.readthedocs.io/en/stable/. I'll
# describe usage of this class below in the code
from geopy.geocoders import Nominatim


# First class is for the News
class NewsAdd:
    def __init__(self):
        # This variable contains file name. This is also example of inheritance: I inherit this variable to the child
        # classes and use it in them without declaring
        self.filename = 'Newsfeed.txt'
        # This variable contains full path of the file. It takes file name and returns file path. Also example of
        # inheritance: i.e. I also inherit this variable to the child classes and use it
        self.filepath = Path(self.filename)
        # To work with geopy.geocoders module, we need to be registered at their site. Variable user_agent requires
        # username. If user with this username is exists, then we can work with geopy.geocoders module.
        self.coordinates_method = Nominatim(user_agent='python_for_dqe')

    # This method writes News headline to the file. text_file variable contains name of file. open_flag variable
    # contains flag for open() module. add_message contains user's News in list format.
    def file_module(self, text_file, open_flag, add_message):
        # counter variable counts number of failed attempt to open a file
        counter = 0
        # pointer variable specified file condition. pointer = True - we can't open file. pointer = False - we
        # successfully open file
        pointer = True
        while pointer is True:
            try:
                # we try to open file
                with open(text_file, open_flag) as AddFile:
                    AddFile.writelines(add_message)
                pointer = False
            except OSError:
                # And if error occurs we increment counter and try to open file one more time
                counter += 1
                print(f'\nNumber of attempt: {counter}. File is not reachable right now.')
                sleep(1)
                # When we tried 3 times, we exit this function and returns to the main method news_type_choice() in the
                # UserChoose class
                if counter == 3:
                    print('\nNumber of attempts was exceeded. Returning to the main menu in 5 seconds')
                    sleep(5)
                    return False
                print('\nTrying to reach file')
                sleep(3)
        return True

    # This method ask user to write the city and check, if this city exists. If not, then method ask user to write new
    # city, otherwise returns city
    def city_check(self):
        # city_flag was created to specify location that exists in the geocode module.
        city_flag = 'no'
        # And while this location does not exist we perform next steps
        while city_flag != 'yes':

            # Ask user to write city
            city_text = input('Please, enter your city: \n')

            # If location is not in the geopy.geocoders module, then we ask user to re-write location name
            while self.coordinates_method.geocode(city_text) is None:
                print(f'Error: Incorrect city name.\n')
                city_text = input('Please, enter your city: \n')

            # And we verify if location that was returned by geopy.geocoders module is what user want
            city_flag = input(f"Is {self.coordinates_method.geocode(city_text, language='en')} your city? Yes/No: \n")
            city_flag = city_flag.lower()

            # If verification flag is not correct, then we ask user to re-write this flag
            while city_flag not in ('yes', 'no'):
                print(f'\nYou enter incorrect command - {city_flag}. Please, write Yes or No\n')
                city_flag = input(
                    f"Is {self.coordinates_method.geocode(city_text, language='en')} your city? Yes/No:\n")
                city_flag = city_flag.lower()
        # After all we return city
        return city_text

    # This method creates News headline and execute method that write this headline to the file. file_flag variable
    # stores flag for file overwriting: if value == Yes then we overwrite file. If value == No, then we add headline
    # to the end of the file. text_message variable contains user's News. text_city variable contains user's city
    def message_module(self, file_flag='No', text_message='Text message', text_city='Vilnius'):

        # We create headline message
        file_text = ['News ----------------------------------------\n', f'{text_message} \n',
                     f"{text_city}, {datetime.now().strftime('%m/%d/%Y %H.%M')} \n",
                     '---------------------------------------------\n\n\n']
        exit_flag = True
        # Firstly we check if file exists
        if self.filepath.is_file():
            # If user wants to overwrite file, we perform next steps
            if file_flag == 'yes':
                exit_flag = NewsAdd().file_module(self.filename, 'w', file_text)
            # If user doesn't want to overwrite file, we perform next steps
            elif file_flag == 'no':
                exit_flag = NewsAdd().file_module(self.filename, 'a', file_text)
        # If file is not exists in the directory, then we create them, logic remains the same as in the block when user
        # wants to overwrite file
        else:
            exit_flag = NewsAdd().file_module(self.filename, 'w', file_text)
        # We return this variable to the main method news_type_choice() from UserChoose class. If exit_flag = True, then
        # we end program execution, if exit_flag = False, then program continue it's work
        return exit_flag

    # This method defines what News user want to write. After defying of user News and City, this method calls method
    # message_module() that create Headline and add it to the file. This is example of encapsulation: all execution
    # operations performs in the other method and user does not see these operations. file_flag variable takes from
    # the class, when user define what type of Add he/she wants to write
    def user_message(self, file_flag):
        # User write News
        news_text = input('\nPlease, write your News: \n')
        while news_text == "":
            news_text = input('You enter empty news. Please, write valid News:\n')
        # User writes city in the another method city_check()
        city_text = NewsAdd().city_check()
        # After all we call method that write user's news to the file
        exit_flag = NewsAdd.message_module(self, file_flag, news_text, city_text)
        return exit_flag


# Second class is for Advertisement news
class AdvAdd(NewsAdd):
    def __init__(self):
        # In the __init__ section we inherit __init__ from the NewsAdd class. That means that we inherit all self.
        # variables and methods from the NewsAdd class
        NewsAdd.__init__(self)

    # This method ask user to write date until Advertisement is active, and check, if this date is correct in
    # formatting or not
    def date_module(self):
        # Date should be in specific format, that's why check, how user writes date
        # pointer specify if data is in correct format or not. while pointer is True then we ask user to re-write date
        pointer = True
        while pointer is True:
            # User writes date until Adv is active
            date_text = input(
                '\nPlease, write date, until which your advertisement will be active in format MM/DD/YYYY. '
                'Exit - end program: \n')
            date_text = date_text.lower()
            if date_text == 'exit':
                print('\nProgram was ended by user')
                return True
            try:
                # If user writes date not in the format MM/DD/YYYY
                date_text = datetime.strptime(date_text, '%m/%d/%Y')
                pointer = False
            except (ValueError, TypeError):
                # Then we print error and ask user to write date again
                print("\nError: Incorrect data format, please, write date in the format MM/DD/YYYY")
        return date_text

    # As in the NewsAdd, this method headline to the file. This is also example of the polymorphism. We inherit method
    # from parent (super-) class and overwrite it in the child class. text_exp_date variable contains date, until Adv
    # is available. Main Logic of the method remains the same, and I will not comment it
    def message_module(self, file_flag='no', text_message='Text message',
                       text_exp_date=datetime(2099, 12, 31)):
        # We create headline message
        file_text = ['Private ad ----------------------------------\n', f'{text_message} \n',
                     f"Actual until {text_exp_date.strftime('%m/%d/%Y')}, "
                     f"{abs((text_exp_date - datetime.now()).days + 1)} days left \n",
                     '---------------------------------------------\n\n\n']
        exit_flag = True
        if self.filepath.is_file():
            if file_flag == 'yes':
                exit_flag = NewsAdd().file_module(self.filename, 'w', file_text)
            elif file_flag == 'no':
                exit_flag = NewsAdd().file_module(self.filename, 'a', file_text)
        else:
            exit_flag = NewsAdd().file_module(self.filename, 'w', file_text)

        return exit_flag

    # As in the NewsAdd, this method defines what user want to write. But we overwrite this method as method ahead to
    # define what Advertisement user want to write
    def user_message(self, file_flag):
        # User writes Adv
        adv_text = input('\nPlease, write your Advertisement: \n')
        while adv_text == "":
            adv_text = input('You enter empty advertisement. Please, write valid Advertisement: \n')
        # We ask user to write date until Adv is active by method date_module()
        date_text = AdvAdd().date_module()
        # If method return True, then we come back to the news_type_choice() method from UserChoose class (main menu)
        if date_text is True:
            return True
        # Date should be more than today's date. If not:
        while date_text <= datetime.today():
            # We raise self-made error and did not stop the execution
            print(f"\nError: You entered date {date_text.strftime('%m/%d/%Y')} less or equal that today's "
                  f"date {datetime.today().strftime('%m/%d/%Y')}. Advertisement can be only with future dates.")
            # And ask user to write date again
            date_text = AdvAdd().date_module()
            # If method return True, then we come back to the news_type_choice() method from UserChoose class (main menu)
            if date_text is True:
                return True
        # And call method that writes Adv to the file
        exit_flag = AdvAdd.message_module(self, file_flag, adv_text, date_text)
        return exit_flag


# Third class is for Unique news
class UniqueAdd(NewsAdd):
    def __init__(self):
        # Again we inherit all variables and methods from NewsAdd class
        NewsAdd.__init__(self)

    # This method has the same logic as module file_module(). But in this time we try to execute API and take response
    # from it
    def api_module(self, api_name, api_body):
        counter = 0
        pointer = True
        while pointer is True:
            try:
                response = requests.get(api_body)
                response.raise_for_status()
                pointer = False
            except requests.exceptions.HTTPError:
                counter += 1
                print(f'\nNumber of attempt: {counter}. API {api_name} is not reachable right now.')
                sleep(1)
                if counter == 3:
                    print('\nNumber of attempts was exceeded. Returning to the main menu in 5 seconds')
                    sleep(5)
                    return False
                print('\nTrying to reach API')
                sleep(3)
        return requests.get(api_body)

    # As in the NewsAdd, this method creates headline. But again we overwrite this method from NewsAdd class.
    # In this state, method create headline that contains today's date, average temperature for the city that user
    # select, and horoscope for the zodiac sign that user select.
    def message_module(self, file_flag='No', city_text='Vilnius', zodiac_sign_text='gemini'):
        # We call API by execution api_module() method to retrieve horoscope for the specific zodiac sign.
        # We do not need to sign up to work with this API
        zodiac_response = UniqueAdd().api_module('zodiac_api', f'https://ohmanda.com/api/horoscope/{zodiac_sign_text}')
        # If response return False, then requests fails, and we need to come back to the main menu
        if zodiac_response is False:
            return False
        # And transform response to the json format
        zodiac_json = zodiac_response.json()

        # Because horoscope for zodiac sign can be too big, we start each sentence from the newline to reduce length
        # of line and make text easier to read
        zodiac_horoscope = zodiac_json['horoscope'].replace('. ', '.\n')

        # We take information of the city, that user defines
        location = self.coordinates_method.geocode(city_text)
        # And from this variable we take latitude and longitude. We will use this information in the API
        location_latitude = round(location.latitude, 2)
        location_longitude = round(location.longitude, 2)

        # We transform today's date to the specific format to use it in the API
        weather_date = datetime.now().strftime('%Y-%m-%d')

        # This API returns forecast information for specific location. We define location by latitude and longitude.
        # Also, we specify date of the forecast. We do not need to sign up to work with this API
        weather_response = UniqueAdd().api_module('weather_api',
                                                  f'https://api.open-meteo.com/v1/forecast?latitude={location_latitude}&'
                                                  f'longitude={location_longitude}&daily=temperature_2m_max,temperature_2m_min&'
                                                  f'timezone=Europe%2FMoscow&start_date={weather_date}&end_date={weather_date}')
        # If response return False, then requests fails, and we need to come back to the main menu
        if weather_response is False:
            return False
        # And we transform response to the json format
        weather_json = weather_response.json()

        # Response returns minimum and maximum temperature for the location in the specific date, and we just calculate
        # average temperature
        average_temperature = round((weather_json['daily']['temperature_2m_max'][0] +
                                     weather_json['daily']['temperature_2m_min'][0]) / 2, 2)
        # Then we create headline message
        file_text = ['Unique message ------------------------------\n',
                     f"Today is {datetime.now().strftime('%d %B, %Y')} \n",
                     f"Average temperature in {city_text.capitalize()} for today is {average_temperature}\n",
                     f"\nAnd today's horoscope for {zodiac_sign_text.capitalize()} zodiac sign is: \n"
                     f"{zodiac_horoscope}",
                     '\n---------------------------------------------\n\n\n']
        # Logic for headline creation remains the same as in the ahead classes. That's why I do not comment it
        exit_flag = True
        if self.filepath.is_file():
            if file_flag == 'yes':
                exit_flag = NewsAdd().file_module(self.filename, 'w', file_text)
            elif file_flag == 'no':
                exit_flag = NewsAdd().file_module(self.filename, 'a', file_text)
        else:
            exit_flag = NewsAdd().file_module(self.filename, 'w', file_text)

        return exit_flag

    # As in the NewsAdd, this method defines what user want to write. But we overwrite this method as method ahead to
    # define what city and zodiac sign user want to write
    def user_message(self, file_flag):
        print("\nThis add creates headline with information about today's day, temperature and horoscope for your "
              "zodiac sign.\n")

        # We ask user to write the city
        city_text = NewsAdd().city_check()

        # Then we create list of zodiac signs
        zodiac_sign_list = ['aquarius', 'pisces', 'aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo',
                            'libra', 'scorpio', 'sagittarius', 'capricorn']

        # Ask user to write his/her zodiac sign
        zodiac_sign_text = input(f"\nPlease, enter your zodiac sign. \nAvailable zodiac signs: "
                                 f"{', '.join(zodiac_sign_list)}.\n")
        zodiac_sign_text = zodiac_sign_text.lower()

        # And check, if this sign is in the list. If it is not, then we ask to re-write sign until sign will be in list
        while zodiac_sign_text not in zodiac_sign_list:
            print(f'\nError: Your zodiac sign {zodiac_sign_text} is incorrect. Available zodiac signs: '
                  f"{', '.join(zodiac_sign_list)}.\n")
            zodiac_sign_text = input('Please, enter your zodiac sign: \n')
            zodiac_sign_text = zodiac_sign_text.lower()

        # After all we call module that writes headline to the file
        exit_flag = UniqueAdd.message_module(self, file_flag, city_text, zodiac_sign_text)
        return exit_flag


# This class defines what Add type we need to write
class UserChoose:
    # Because I did not create __init__ in this class I specified this method as static. In that case, we can do not
    # use self in the method variables
    @staticmethod
    def news_type_choice():
        # In order to stay in the main menu I create while... statement while exit_flag is False we always will be in
        # the main menu. Even if some error will happen in API or file parsing. Variable exit_flag returns from all
        # methods user_module()
        exit_flag = False
        while exit_flag is False:
            # We ask user if he/she wants to overwrite file
            file_flag = input('\nDo you want to re-write the file? Yes/No. Exit - end program: \n')
            file_flag = file_flag.lower()

            # If user want to exit the program, we end our program by return
            if file_flag == 'exit':
                return 'Program was ended by user'

            # If flag for re-writing is incorrect, we ask user to write flag once again
            while file_flag not in ('yes', 'no'):
                print(f'You enter incorrect command - {file_flag} - for file re-writing. Please, write Yes or No')
                file_flag = input('Do you want to re-write the file? Yes/No Exit - end program: \n')
                file_flag = file_flag.lower()
                # User still able to exit program
                if file_flag == 'exit':
                    return 'Program was ended by user'

            # We ask user what type of Add he/she wants to write
            add_type = input('What type of Add do you want to write? News/Adv/Unique. Exit - end program: \n')
            add_type = add_type.lower()

            # User still able to exit program
            if add_type == 'exit':
                return 'Program was ended by user'

            # while flag for Add is incorrect, we ask user to re-write it
            while add_type not in ('news', 'adv', 'unique'):
                print(
                    f'You enter incorrect command - {add_type} - for Add choosing. Please, write News or Adv or Unique')
                add_type = input('What type of Add do you want to write? News/Adv/Unique. Exit - end program: \n')
                add_type = add_type.lower()
                # User still able to exit program
                if add_type == 'exit':
                    return 'Program was ended by user'

            # And then depending on flag we call classes
            if add_type == 'news':
                # On the first parameter we take own class because we need to define self part
                exit_flag = NewsAdd.user_message(NewsAdd(), file_flag)
            elif add_type == 'adv':
                exit_flag = AdvAdd.user_message(AdvAdd(), file_flag)
            elif add_type == 'unique':
                exit_flag = UniqueAdd.user_message(UniqueAdd(), file_flag)


if __name__ == "__main__":
    # And in the global scope we just call method from one class
    UserChoose().news_type_choice()
