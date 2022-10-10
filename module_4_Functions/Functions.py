# To enable working with random numbers we need to import library 'random'
import random
# I import module string to change creation of the list with latin letters, according to the mentor's notes.
import string
# I will use this module in the 3 module 'String Object'
import re

# Module 2 Collections
# Home task 1 - create a list of random number of dicts (from 2 to 10)


# Because user define range for the dicts, we need to validate that this range is correct. To do this, I create 2
# functions dict_range_validation and dict_range_creation. dict_range_validation check that range borders are under
# condition. If not, then this function ask user to re-create borders.
def dict_range_validation(left_border_for_dict, right_border_for_dict):

    # Error resolving if left border > or = than right border
    while left_border_for_dict >= right_border_for_dict:
        print(f"Error: left border value {left_border_for_dict} is equal or higher that right border value "
              f"{right_border_for_dict}")
        left_border_for_dict = int(input("Please, enter left border for dict's range creation: \n"))
        right_border_for_dict = int(input("Please, enter right border for dict's range creation: \n"))

    # Error resolving if left or right border is not in range
    while left_border_for_dict not in range(2, 101) or right_border_for_dict not in range(2, 101):
        if left_border_for_dict not in range(2, 101):
            print(f"Error: left border value {left_border_for_dict} not in the range from 2 to 100")
            left_border_for_dict = int(input("Please, enter left border for dict's range creation: \n"))
        elif right_border_for_dict not in range(2, 101):
            print(f"Error: right border value {right_border_for_dict} not in the range from 2 to 100")
            right_border_for_dict = int(input("Please, enter right border for dict's range creation: \n"))
    # And after all checks function return left and right border
    return left_border_for_dict, right_border_for_dict


# Function dict_range_creation contains logic of dicts range creation. In this function user select left and
# round boundaries of the range. Then some possible user errors are processed by checks in this function and execution
# of dict_range_validation function that also has some checks
def dict_range_creation():
    # Just printed some notes and rules to the user
    print("\n In this task we have list with dicts. From the requirements we have length of list, but not of dicts. "
          "That's why you can set length of dicts manually. You will write range borders. Length of dict will be "
          "generated in this range. Please note that we have limit of range from 2 to 100, but anyway length of dict "
          "can be no longer than 26 key:value pars, because we have 26 unique letters in the english language. "
          "Please note, that left border should be less than right border. \n")

    # Then user selects left and right borders. I convert values to int by int() method because as a default values
    # from import are string
    left_border_for_dict = int(input("Please, enter left border for dict's range: \n"))
    right_border_for_dict = int(input("Please, enter right border for dict's range: \n"))

    # While left and right border are not fit conditions, we call function that create new borders. Check ends,
    # when borders will be under conditions.
    while (left_border_for_dict >= right_border_for_dict) or \
            (left_border_for_dict not in range(2, 101)) or (right_border_for_dict not in range(2, 101)):
        left_border_for_dict, right_border_for_dict = dict_range_validation(left_border_for_dict, right_border_for_dict)

    # return checked and ready left and right borders as variables
    return left_border_for_dict, right_border_for_dict


# Function collections_task_1 contains logic of list with dicts creation. Was deleted code that checks if key already
# exists in the dict. Now if key is exists in the dict, then value will be overwrited by the new one.
def collections_task_1():
    # Create list with dicts before work
    list_with_dicts = []

    # Create list with letters by string method ascii_lowercase()
    list_with_letters = list(string.ascii_lowercase)

    # Call function dict_range_creation() that returns created by user values of left and right range border
    left_border_for_dict, right_border_for_dict = dict_range_creation()

    # first for... statement is for appending dicts to the list. We assume that in the list can be from 2 to 10 dicts
    for i in range(random.randint(2, 10)):
        # Create temporary dict for dicts creation
        temporary_dict = {}
        # second for... statement is for dicts creation. Length of the dict is still random, but now user specified the
        # random range
        for j in range(random.randint(left_border_for_dict, right_border_for_dict)):
            # In this for... statement we just take random key and generate value for it
            letter_for_dict = list_with_letters[random.randint(0, len(list_with_letters) - 1)]
            temporary_dict[letter_for_dict] = random.randint(0, 100)
        # And after all we append dict to the list
        list_with_dicts.append(temporary_dict)
    # And return our list
    return list_with_dicts


# Module 2 Collections
# Home task 2 - get previously generated list of dicts and create one common dict

# Function collections_task_2_1 contains 1 part of the logic that creates final dict. Code in this function remains
# the same as in the file 'Collections.py'. That's why I didn't add the same commentary as in the 2 module homework
# except new lines of code this function requires 1 (list that was created by the collections_task_1() function
# parameter before execution
def collections_task_2_1(list_with_dicts):

    result_dict_keys = []
    result_dict_values = []
    result_dict_keys_temporary = []

    for i in range(len(list_with_dicts)):
        for key in list_with_dicts[i]:
            for j in range(len(result_dict_keys)):
                result_dict_keys_temporary[j] = result_dict_keys[j][:1]
            if key in result_dict_keys_temporary:
                result_dict_index = result_dict_keys_temporary.index(key)
                if list_with_dicts[i][key] > result_dict_values[result_dict_index]:
                    index_for_new_dict = str(key) + '_' + str(i+1)
                    result_dict_keys[result_dict_index] = index_for_new_dict
                    result_dict_values[result_dict_index] = list_with_dicts[i][key]
                    result_dict_keys_temporary[result_dict_index] = index_for_new_dict
            else:
                result_dict_keys.append(key)
                result_dict_values.append(list_with_dicts[i][key])
                result_dict_keys_temporary.append(key)
    # Return pre-ready keys and values as two different lists
    return result_dict_keys, result_dict_values


# Function collections_task_2_2 contains 2 part of the logic that creates final dict. Code in this function remains
# the same as in the file 'Collections.py'. That's why I didn't add the same commentary as in the 2 module homework
# except new lines of code this function requires 3 parameters (lists that was created by the collections_task_2_1()
# and collections_task_1() functions before execution
def collections_task_2_2(result_dict_keys, result_dict_values, list_with_dicts):

    result_dict_keys_temporary = []
    result_dict_dict_index_temporary = []

    result_dict = {}

    for i in range(len(list_with_dicts)):
        for key in list_with_dicts[i]:
            if key in result_dict_keys:
                if key not in result_dict_keys_temporary:
                    result_dict_keys_temporary.append(key)
                    result_dict_dict_index_temporary.append(i+1)
                else:
                    key_index = result_dict_keys_temporary.index(key)
                    result_dict_keys[result_dict_keys.index(key)] = str(key) + '_' + \
                        str(result_dict_dict_index_temporary[key_index])

    for i in range(len(result_dict_keys)):
        result_dict[result_dict_keys[i]] = result_dict_values[i]

    # And we return final dict
    return result_dict


if __name__ == "__main__" :
    # Firstly we call function collections_task_1(). It generates list with dicts and return it. We collect this list to
    # variable 'result_list'
    result_list = collections_task_1()

    # Let's print our list
    print(f'\nHome task 1 - create a list of random number of dicts, result list: \n {result_list} \n')

    # Then we call function collections_task_2_1(). This function takes list with dicts as required parameter and returns
    # pre-ready keys and values. We store pre-ready keys in variable final_dict_keys and values in final_dict_values
    final_dict_keys, final_dict_values = collections_task_2_1(result_list)

    # At the end we call function collections_task_2_2(). This function takes pre-ready keys and values and list with dicts.
    # Function returns final dict and we store it in the variable final_dict
    final_dict = collections_task_2_2(final_dict_keys, final_dict_values, result_list)

    # Let's print our final dict
    print(f'Home task 2 - create one dict with from list of dicts, result dict: \n {final_dict} \n')


# Module 3 String Object

# Function sentence_transformation contains logic of sentence transformation. I move this logic to the separate
# function to reduce the code
def sentence_transformation(sentence):

    sentence = sentence.replace('\n', ' ')
    sentence = sentence.strip()
    sentence = sentence.lower()
    sentence = sentence.capitalize()
    # After all transformation I return ready sentence
    return sentence


# Function string_task contains main logic of the 3 module. In this function I create final text, new sentence
# which consists of last words in all sentences and count whitespaces in the original text
def string_task():

    variable_with_original_text = """
homEwork:

  tHis iz your homeWork, copy these Text to variable.

 

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

 

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

 

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

    space_count = variable_with_original_text.count('\u0020')

    variable_with_original_text = variable_with_original_text.lower()
    variable_with_original_text = variable_with_original_text.strip()
    variable_with_original_text = re.sub(' iz ', ' is ', variable_with_original_text)
    variable_with_original_text = re.sub('“iz”', ' “iz”', variable_with_original_text)
    variable_with_original_text = re.sub('tex\.', 'text.', variable_with_original_text)

    last_sentence = ''

    for sentence in re.split('\.|!|\?', variable_with_original_text):
        if (sentence != '\u0020') and (sentence != '\n') and (sentence != ''):
            sentence_list = sentence.split(' ')
            last_word = sentence_list[len(sentence_list) - 1]
            last_sentence += last_word + ' '

    final_text = ''
    is_upper_flag = 0
    text_index = 0

    for letter in variable_with_original_text:
        if is_upper_flag != 1:
            if letter.isalpha():
                is_upper_flag = 1
                final_text += variable_with_original_text[text_index].capitalize()
            else:
                final_text += letter
        else:
            final_text += letter
            if letter in r'\.|!|\?':
                is_upper_flag = 0
        text_index += 1

    # In the line 239 I call the function sentence_transformation() that performs transformation of the sentence.
    # After all, I take ready and beautiful sentence
    last_sentence = sentence_transformation(last_sentence)
    last_sentence += '.'

    final_text += ' ' + last_sentence

    # And I just return final text and number of whitespaces in the initial text
    return final_text, space_count


if __name__ == "__main__":
    # I call function string_task() with main logic and take 2 arguments (final text and number of whitespaces) from it
    ready_text, final_count = string_task()
    # After all, I print final text and number of whitespaces in the original text
    print('\nTransformed text with added sentence:\n\n', ready_text)
    print('\nNumber of whitespaces from original text:', final_count)
