# To enable working with random numbers we need to import library 'random'
import random
# I import module string to change creation of the list with latin letters, according to the mentor's notes.
import string
# I will use this module in the 3 module 'String Object'
import re

# Module 2 Collections
# Home task 1 - create a list of random number of dicts (from 2 to 10)


# 1 function contains logic of dicts range creation. In this function user select left and round boundaries of the
# range. And some possible user errors are processed
def dict_range_creation():
    # Just printed some notes and rules to the user
    print("\n In this task we have list with dicts. From the requirements we have length of list, but not of dicts. "
          "That's why you can set length of dicts manually. You will write range borders. Length of dict will be "
          "generated in this range. Please note that we have limit of range from 2 to 100, but anyway length of dict"
          "can be no longer than 26 key:value pars, because we have 26 letters in the english language. "
          "Left border should be less than right border \n")

    # Then user selects left and right borders. I convert values to int by int() method because as a default values
    # from import are string
    left_border_for_dict = int(input("Please, enter left border for dict's range: \n"))
    right_border_for_dict = int(input("Please, enter right border for dict's range: \n"))

    # Error resolving if left border > or = than right border
    while left_border_for_dict >= right_border_for_dict:
        print(f"Error: left border value {left_border_for_dict} is higher that right border {right_border_for_dict}")
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

    # return left and right borders as variables
    return left_border_for_dict, right_border_for_dict


# 2 function contains logic of list with dicts creation. Was deleted code that checks if key already exists in the dict.
# Now if key is exists in the dict, then value will be overwrited by the new one.
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

# 3 function contains 1 part of the logic that creates final dict. Code in this function remains the same as in the file
# 'Collections.py'. That's why I didn't add the same commentary as in the 2 module homework except new lines of code
# This function requires 1 (list that was created by the collections_task_1() function parameter before execution
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


# 4 function contains 2 part of the logic that creates final dict. Code in this function remains the same as in the file
# # 'Collections.py'. That's why I didn't add the same commentary as in the 2 module homework except new lines of code
# This function requires 3 parameters (lists that was created by the collections_task_2_1() and collections_task_1()
# functions before execution
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

def sentence_transformation(sentence):

    sentence = sentence.replace('\n', ' ')
    sentence = sentence.strip()
    sentence = sentence.lower()
    sentence = sentence.capitalize()

    return sentence


def string_task():

    variable_with_original_text = """
    homEwork:

        tHis iz your homeWork, copy these Text to variable.
        
        
        
        You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.
        
        
        
        it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.
        
        
        
        last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
    """

    text_list = []

    for sentence in variable_with_original_text.split('.'):
        text_list.append(sentence)

    ready_text = ''
    last_sentence = ''

    for i in range(len(text_list) - 1):
        text_list[i] = sentence_transformation(text_list[i])
        text_list[i] = re.sub(' iz ', ' is ', text_list[i])
        text_list[i] = re.sub('“iz”', ' “is” ', text_list[i])
        text_list[i] = re.sub(r'tex$', 'text', text_list[i])
        text_list[i] = re.sub(r'\s+', ' ', text_list[i])
        first, *middle, last = text_list[i].split()
        if not last.isdigit():
            last_sentence += last + ' '
        else:
            last_sentence += middle[-1] + ' '
        ready_text += text_list[i] + '. '

    last_sentence = sentence_transformation(last_sentence)
    last_sentence += '.'
    ready_text = ready_text + last_sentence

    space_count = variable_with_original_text.count('\u0020')

    return ready_text, space_count


final_text, final_count = string_task()

print('\nTransformed text with added sentence:\n\n', final_text)
print('\nNumber of whitespaces from original text:', final_count)
