# I import library re because I will use method sub from it to replace some words
import re

# Firstly we need to create variable with original text
variable_with_original_text = """
homEwork:

  tHis iz your homeWork, copy these Text to variable!



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE?



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87. """


# Firstly I transform all letters to lowercase by .lower() method.
variable_with_original_text = variable_with_original_text.lower()
# Then I correct expression 'iz' to 'is' by replacing method .sub() from library re. I do not use any regex
# patterns here because there is actually no need in that case. All misspelling happens in independent expressions,
# not in the words (i.e. word like 'existing'). That's why I use only spaces to avoid replacing in the words like
# 'normalize'.
variable_with_original_text = re.sub(' iz ', ' is ', variable_with_original_text)
# In the line 31 I add spaces to the "iz" because in original text this expression was glued with the previous word
variable_with_original_text = re.sub('“iz”', ' “iz”', variable_with_original_text)
# I also notice that we have 'tex.' expression in the end of the sentence 'last iz TO calculate nuMber
# OF Whitespace characteRS in this Tex.' I also decide to replace it by word 'text'.
variable_with_original_text = re.sub('tex\.', 'text.', variable_with_original_text)

# I create variable for the last sentence, that will contain my own sentence
last_sentence = ''

# Then I parse whole text by splitting it to the sentences. Delimiters are '.', '!', '?'
for sentence in re.split('\.|!|\?', variable_with_original_text):
    # There are some possibilities that sentence will be just whitespace. In that case first, *middle, last will not
    # work. That's why I firstly check, if sentence contains only whitespace
    if (sentence != '\u0020') and (sentence != '\n') and (sentence != ''):
        # If sentence contains letters then I split each words to three variables. Variable 'first' contains first word
        # of the sentence. Variable 'last' contains the last word of the sentence. Variable (or it is better to say
        # array or *args) '*middle' contains all other words (we can say words that is not first and last in the
        # sentence). We will work with 'last' variable only.
        first, *middle, last = sentence.split()
        # In the task requirements we need to create last sentence with last words. We just add value from 'last'
        # variable to our variable 'last_sentence' with a space
        last_sentence += last + ' '

# Then I create variable for the transformed text
final_text = ''
# Also create variable for flag. I explain the logic of this flag below
is_upper_flag = 0
# This variable contains index of each element. Because I am going to parse text by each letter, I need to know what
# index in the text this letter have.
text_index = 0

# Then I parse whole text by each letter
for letter in variable_with_original_text:
    # The logic of the upper flag is the next: this flag is looking for the first letter in the sentence and the
    # symbols that end sentence. If is_upper_flag == 0 then we look for first letter in the sentence. When we find this
    # letter, we set is_upper_flag = 1. In that case we are looking for the symbols that end sentence (., !, ?). When
    # we find this symbol we set is_upper_flag = 0. And logic starts again.
    if is_upper_flag != 1:
        # If letter variable is actual letter, then we assume, that this letter is the first in the sentence. In that
        # case we:
        if letter.isalpha():
            # we set upper_flag = 1
            is_upper_flag = 1
            # and add to the final_text upper letter
            final_text += variable_with_original_text[text_index].capitalize()
        else:
            # if letter variable is not the actual letter then we just add this symbol to the final_text
            final_text += letter
    else:
        # if upper_flag = 1 we still add symbol to the final_text
        final_text += letter
        # And check if this symbol is the symbol that ends sentence. If it is, then we:
        if letter in r'\.|!|\?':
            # We set upper_flag = 0
            is_upper_flag = 0
    # After all operation we increment index
    text_index += 1

# We still need to perform some operation with the last sentence. Firstly I delete all spaces from the start and the end
# of the sentence
last_sentence = last_sentence.strip()
# Then I transform each letter of the sentence to lowercase
last_sentence = last_sentence.lower()
# Then I transform first letter of the sentence to uppercase
last_sentence = last_sentence.capitalize()
# Finally I add a dot to the end of the sentence
last_sentence += '.'

# After all operations of original text transforming we add symbol from list end_symbols to each sentence,
# because we lost it when parsed original text. Each symbol from end_symbols list corresponds to its sentence
final_text += last_sentence

# And print it
print('\nTransformed text with added sentence:\n\n', final_text)

# Also we need to count all whitespaces in the original text. To do this I use unicode combination that represents
# whitespace symbol. Unfortunately, I count only 83 symbols. I also tried another unicode combinations with property
# of whitespace (you can find list of unicode combinations here: http://xahlee.info/comp/unicode_whitespace.html) but
# almost all of them returns 0, except of lines count. Maybe I incorrectly paste the original text, but for now,
# I don't know any solutions to count 87 whitespaces
print('\nNumber of whitespaces from original text:', variable_with_original_text.count('\u0020'))
