import re
import csv


# this class and it's methods are imported to the file 'Module_Files.py'. To use this method you need to execute
# file 'Module_Files.py'.
class CsvParsing:
    # method word_count() counts number of words and write results to the .csv file word_count
    def word_count(self, newsfeed_file_path="Newsfeed.txt"):

        list_word = []
        # try to open newsfeed file
        try:
            with open(newsfeed_file_path, 'r', encoding="utf-8") as newsfeed_file:
                # Read all from file
                news_text = newsfeed_file.read()
                # split all text by whitespace
                news_text = news_text.split()
                for text in news_text:
                    # delete words that not match the pattern (for example word abc--dce will be deleted because have
                    # 2 symbols '-')
                    text = re.sub(r'[^a-zA-Z0-9а-яА-Я_-]+|-{2,}', '', text)
                    # if word matchs pattern
                    if re.match(r'[a-zA-Z0-9а-яА-Я_]+|[a-zA-Z0-9а-яА-Я_]+-[a-zA-Z0-9а-яА-Я_]+', text):
                        # and if word is not full digit
                        if not text.isdigit():
                            # then we lower this word
                            text = text.lower()
                            # and add it to the list
                            list_word.append(text)
        # if we can't open file, we raise an error and end the program
        except IOError:
            print("\nError: Can't open newsfeed file")
            return False

        word_count_dict = {}
        # we count occurrences of all words in a list and write result in a dict as key:value (word:number of
        # occurrences)
        for word in list_word:
            if word in word_count_dict:
                word_count_dict[word] += 1
            else:
                word_count_dict[word] = 1
        # we try to open .csv file
        try:
            # with a newline as ''
            with open('word_count.csv', 'w', newline='', encoding="utf-8") as word_count_csv:
                # create headers
                headers = ['Word', 'Count']
                # create writer
                csv_writer = csv.DictWriter(word_count_csv, fieldnames=headers)
                # write headers
                csv_writer.writeheader()
                # change writer
                csv_writer = csv.DictWriter(word_count_csv, fieldnames=headers, quoting=csv.QUOTE_ALL)
                # and write all result in a quotes
                for key, value in word_count_dict.items():
                    csv_writer.writerow({'Word': key, 'Count': value})
        # if we can't open .csv file we raise an error end end the program
        except IOError:
            print("\nError: Can't process csv file with words count")
            return False

    # method letter_count counts occurrences of letters
    def letter_count(self, newsfeed_file_path="Newsfeed.txt"):
        # this letter contains letters
        list_letter = []
        # this list contains number of occurrences for each letter
        letter_count_all_list = []
        # this list contains number of occurrences for capital letter
        letter_count_upper_list = []
        # we try to open .csv file
        try:
            with open(newsfeed_file_path, 'r', encoding="utf-8") as newsfeed_file:
                news_text = newsfeed_file.read()
                # for each symbol in the text
                for symbol in news_text:
                    # we look only for latin letters
                    if symbol.isalpha():
                        # if symbol already in a list
                        if symbol.lower() in list_letter:
                            # then we increment value on the same position in the list letter_count_all_list as in the
                            # list letter_count
                            letter_count_all_list[list_letter.index(symbol.lower())] += 1
                            # if letter is in upper case
                            if symbol.isupper():
                                # then we perform the same for letter_count_upper_list list
                                letter_count_upper_list[list_letter.index(symbol.lower())] += 1
                        # if letter is not in the letter_list
                        else:
                            # then we add it to the list_letter
                            list_letter.append(symbol.lower())
                            # and add 1 number as first occurrence of this letter
                            letter_count_all_list.append(1)
                            # if letter is in upper case
                            if symbol.isupper():
                                # we add 1 number as first occurrence of the upper case letter
                                letter_count_upper_list.append(1)
                            else:
                                # if not - we add 0 as none occurrence of the upper case letter
                                letter_count_upper_list.append(0)
        # if we can't open .csv file we raise an error and end the program
        except IOError:
            print("\nError: Can't process newsfeed file")
            return False

        # then we count percentage of occurrences for each letter
        letter_percentage_list = []
        for i in range(len(list_letter)):
            # as number of letter occurrence / all letters occurrence
            letter_percentage_list.append(round(letter_count_all_list[i] / sum(letter_count_all_list) * 100, 3))

        # we try to open .csv file
        try:
            with open('letter_count.csv', 'w', newline='', encoding="utf-8") as word_count_csv:
                # create headers
                headers = ['Letter', 'Count_All', 'Count_Uppercase', 'Percentage']
                # create writer
                csv_writer = csv.DictWriter(word_count_csv, fieldnames=headers)
                # write headers
                csv_writer.writeheader()
                # change writer
                csv_writer = csv.DictWriter(word_count_csv, fieldnames=headers, quoting=csv.QUOTE_ALL)
                # write result in the quotes to the .csv file
                for i in range(len(list_letter)):
                    csv_writer.writerow({'Letter': list_letter[i], 'Count_All': letter_count_all_list[i],
                                         'Count_Uppercase': letter_count_upper_list[i],
                                         'Percentage': letter_percentage_list[i]})
        # if we can't open .csv file we raise an error and end the program
        except IOError:
            print("\nError: can't process csv file with letters count")
            return False


if __name__ == "__main__":
    CsvParsing().word_count()
    CsvParsing().letter_count()

