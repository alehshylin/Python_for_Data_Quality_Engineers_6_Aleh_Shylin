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
print(f'\nHome task 1 - create a list of random number of dicts, result list: \n {list_with_dicts} \n')


# Home task 2 - get previously generated list of dicts and create one common dict

# Let's create empty dict firstly
result_dict = {}
# And related for this dict lists, result_dict_keys - for keys in the future dict;
# result_dict_values - for values in the future dict;
# result_dict_keys_temporary - to transformation composite keys to one symbol (i.e. from 'x_2' to 'x')
result_dict_keys = []
result_dict_values = []
result_dict_keys_temporary = []

# First for... statement was created for list parsing
for i in range(len(list_with_dicts)):
    # Second for... statement was created for dict parsing. By accessing list by index we can work with the dict.
    for key in list_with_dicts[i]:
        # In this case I parse keys from list with true keys and convert them to one symbol (i.e. from 'q_2' to 'q')
        for j in range(len(result_dict_keys)):
            result_dict_keys_temporary[j] = result_dict_keys[j][:1]
        # I perform the convertation to one symbol for this if... statement.
        # Because all keys from old dict are as one symbol. And if key from old dict is in the list of new dict keys
        # we perform next steps
        if key in result_dict_keys_temporary:
            # I take index from 'result_dict_keys' list to send it to the 'result_dict_values' list because
            # one position in both list corresponds to the one key:value pars in the dict
            result_dict_index = result_dict_keys_temporary.index(key)
            # If key already exists in the new dict (i.e. that key exists in the list 'result_dict_keys'), we compare
            # values from old dict and the new dict (we take values from list 'result_dict_values').
            if list_with_dicts[i][key] > result_dict_values[result_dict_index]:
                # If value from the old dict is greater than value from new dict, we create key as key_{number_of_dict}.
                # Please note, that dict numeration is going from 0.
                # So, that means that 'q_1' key is from the 2 dict, not the first.
                index_for_new_dict = str(key) + '_' + str(i)
                # And I rewrite values in all three lists
                result_dict_keys[result_dict_index] = index_for_new_dict
                result_dict_values[result_dict_index] = list_with_dicts[i][key]
                # I perform operation in the line 76 to make sure that length of the 'result_dict_keys_temporary' will
                # be the same as length of the 'result_dict_keys' list.
                result_dict_keys_temporary[result_dict_index] = index_for_new_dict
        else:
            # If key doesn't exist in the new dict (in the list 'result_dict_keys') then we just add values to all three lists
            result_dict_keys.append(key)
            result_dict_values.append(list_with_dicts[i][key])
            # I perform operation in the line 85 to make sure that length of temporary list will be the same as the
            # length of the main two lists (result_dict_keys and result_dict_values). That means that in each
            # overwriting of the temporary list, values in this list will be in the same position
            # (will have the same index), as values in the list 'result_dict_keys'
            result_dict_keys_temporary.append(key)


# Approach in the lines 94-119 does not change keys that is presented only once in the whole list from task 1. Only
# those keys, that have duplicates (or you can call pars) in the list from task 1. As an example: we have a list
# [{a:12,d:31,c:90,s:12,w:31}, {e:24,q:52,a:10,x:32,z:32}]. As a result, this approach will take only 'a' key and
# transform it to the 'a_0':12. Other keys will not be transformed because there are unique in the list.

# Firstly, let's create lists that will hold keys and their dict number
result_dict_keys_temporary = []
result_dict_dict_index_temporary = []

# We parse list with dicts from task 1 in this for... statement
for i in range(len(list_with_dicts)):
    # We parse each dict by key
    for key in list_with_dicts[i]:
        # if key from old dicts (from task 1) is in the list of the keys of the new dict (that was partially created
        # in the lines 51-85), then it means, that this key doesn't have dict number in the end (for example doesn't
        # have '_4' symbol, only 'q'). And we work work these keys
        if key in result_dict_keys:
            # In the section from line 106 to line 119 we try to find keys which are repeated. If there are repeated,
            # this means that first appended key has maximum value, others same keys will have less values.
            if key not in result_dict_keys_temporary:
                result_dict_keys_temporary.append(key)
                result_dict_dict_index_temporary.append(i)
            # When we find the same second key, we assumed, that first key has maximum value. And we perform next steps.
            else:
                # We find index of the first key with maximum values
                key_index = result_dict_keys_temporary.index(key)
                # And we rewrite key name in the list that was used for dict creation in the lines 51-91. For example
                # from 'h' to 'h_5' if the first appearance of 'h' key was in the 6 dict in the list from 1 task and
                # we have second (or third, of fourth and so on) appearance of the same 'h' key
                result_dict_keys[result_dict_keys.index(key)] = str(key) + '_' + \
                    str(result_dict_dict_index_temporary[key_index])

# In this for... statement I parse lists with keys and values to create dict
for i in range(len(result_dict_keys)):
    result_dict[result_dict_keys[i]] = result_dict_values[i]

# Let's print our result dict
print(f'Home task 2 - create one dict with from list of dicts, result dict: \n {result_dict}')
