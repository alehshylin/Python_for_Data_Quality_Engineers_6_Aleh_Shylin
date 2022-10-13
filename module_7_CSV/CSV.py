import re
import csv


class CsvParsing:

    def word_count(self, newsfeed_file_path="Newsfeed.txt"):

        list_word = []
        try:
            with open(newsfeed_file_path, 'r') as newsfeed_file:
                news_text = newsfeed_file.read()
                news_text = news_text.split()
                for text in news_text:
                    text = re.sub(r'[^a-zA-Z0-9_-]+|-{2,}', '', text)
                    if re.match(r'[a-zA-Z0-9_]+|[a-zA-Z0-9_]+-[a-zA-Z0-9_]+', text):
                        if not text.isdigit():
                            text = text.lower()
                            list_word.append(text)
        except IOError:
            print("\nError: Can't open newsfeed file")
            return False

        word_count_dict = {}
        for word in list_word:
            if word in word_count_dict:
                word_count_dict[word] += 1
            else:
                word_count_dict[word] = 1
        try:
            with open('word_count.csv', 'w', newline='') as word_count_csv:
                headers = ['Word', 'Count']
                csv_writer = csv.DictWriter(word_count_csv, fieldnames=headers)
                csv_writer.writeheader()
                csv_writer = csv.DictWriter(word_count_csv, fieldnames=headers, quoting=csv.QUOTE_ALL)
                for key, value in word_count_dict.items():
                    csv_writer.writerow({'Word': key, 'Count': value})
        except IOError:
            print("\nError: Can't process csv file with words count")
            return False

    def letter_count(self, newsfeed_file_path="Newsfeed.txt"):

        list_letter = []
        letter_count_all_list = []
        letter_count_upper_list = []
        try:
            with open(newsfeed_file_path, 'r') as newsfeed_file:
                news_text = newsfeed_file.read()
                for symbol in news_text:
                    if symbol.isalpha():
                        if symbol.lower() in list_letter:
                            letter_count_all_list[list_letter.index(symbol.lower())] += 1
                            if symbol.isupper():
                                letter_count_upper_list[list_letter.index(symbol.lower())] += 1
                        else:
                            list_letter.append(symbol.lower())
                            letter_count_all_list.append(1)
                            if symbol.isupper():
                                letter_count_upper_list.append(1)
                            else:
                                letter_count_upper_list.append(0)
        except IOError:
            print("\nError: Can't process newsfeed file")
            return False

        letter_percentage_list = []
        for i in range(len(list_letter)):
            letter_percentage_list.append(round(letter_count_all_list[i] / sum(letter_count_all_list), 3))

        try:
            with open('letter_count.csv', 'w', newline='') as word_count_csv:
                headers = ['Letter', 'Count_All', 'Count_Uppercase', 'Percentage']
                csv_writer = csv.DictWriter(word_count_csv, fieldnames=headers)
                csv_writer.writeheader()
                csv_writer = csv.DictWriter(word_count_csv, fieldnames=headers, quoting=csv.QUOTE_ALL)
                for i in range(len(list_letter)):
                    csv_writer.writerow({'Letter': list_letter[i], 'Count_All': letter_count_all_list[i],
                                         'Count_Uppercase': letter_count_upper_list[i],
                                         'Percentage': letter_percentage_list[i]})
        except IOError:
            print("\nError: can't process csv file with letters count")
            return False


if __name__ == "__main__":
    CsvParsing().word_count()
    CsvParsing().letter_count()

