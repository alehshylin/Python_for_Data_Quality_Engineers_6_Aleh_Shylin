# To enable working with random numbers we need to import library 'random'
import random


# Home task 1 - create a list of random number of dicts (from 2 to 10)

# Before append dicts to the list let's create list
list_with_dicts = []

# In the 16 line I create a list with latin letters in lowercase. To do this I use next methods: list() - to create list
# map() - returns the result of operation in the list format. It is like small for... section in one line.
# chr() - method that converts integer to the unicode character. Unicode with indexes from 97 to 123 is a latin letters
# in lowercase. In the other words, we can write next statement:
# 'for i in range(97,123): list_with_letters.append(chr(i))'. And this statement will return same result as statement
# in map() method
list_with_letters = list(map(chr, range(97, 123)))

# first for... statement is for appending dicts to the list. We assume that in the list can be from 2 to 10 dicts
for i in range(random.randint(2, 10)):
    # Create temporary dict for dicts creation
    temporary_dict = {}
    # second for... statement is for dicts creation. We assume that in the dict can be from 3 to 10 key:value pars
    for j in range(random.randint(3, 10)):
        # In this section we write letter to new variable 'letter_for_dict' and check if this letter is already
        # in the dict. If it is, then we generate new letter. The reason of this is that we can generate letter
        # that is already used as key in the dict. In that case old value will be overwrited by the new value and
        # length of dict will be smaller by one item in one iteration. To prevent this I use while statement.
        letter_for_dict = list_with_letters[random.randint(0, len(list_with_letters) - 1)]
        # I generate new key each time if key is already exists in the dict
        while letter_for_dict in temporary_dict:
            letter_for_dict = list_with_letters[random.randint(0, len(list_with_letters) - 1)]
        # After we made sure that letter (key) is unique, we add this letter (key) with value into the dict
        temporary_dict[letter_for_dict] = random.randint(0, 100)
    # After the end of the second for... statement we come back to the first one and append dict to the list
    list_with_dicts.append(temporary_dict)

# Let's print our list
print(list_with_dicts, '\n')


# Home task 2 - get previously generated list of dicts and create one common dict

# Let's create empty dict firstly
result_dict = {}

# First for... statement was created for list parsing
for i in range(len(list_with_dicts)):
    # Second for... statement was created for dict parsing. By accessing list by index we can work with the dict.
    for key in list_with_dicts[i]:
        # In this if... statement we check that key from dict from list (from the first task) is exists in the
        # new dict (result_dict)
        if key in result_dict:
            # If key already exists in the new dict, we compare values from old dict and the new dict.
            if list_with_dicts[i][key] > result_dict[key]:
                # If value from the old dict is greater than value from new dict, we create key as key_{number_of_dict}.
                # Please note, that dict numeration is going from 0.
                # So, that means that 'q_1' key is from the 2 dict, not the first.
                index_for_new_dict = str(key) + '_' + str(i)
                # We delete key:value pars from the new dict by the old key name and old value
                result_dict.pop(key)
                # And add key:value pars with the new key name and value
                result_dict[index_for_new_dict] = list_with_dicts[i][key]
        else:
            # If key doesn't exist in the new dict then we just add key:value pars
            result_dict[key] = list_with_dicts[i][key]

# Let's print our result dict
print(result_dict)
