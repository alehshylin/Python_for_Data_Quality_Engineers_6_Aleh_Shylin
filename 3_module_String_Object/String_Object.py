# I import library re because I will use method sub from it to replace some words
import re

# Firstly we need to create variable with original text
variable_with_original_text = """
homEwork:

  tHis iz your homeWork, copy these Text to variable.

 

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

 

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

 

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

# I create list to parse original text in it. Each element of this list stores one sentence from original text
text_list = []

# In this for... statement I parse original text to the list. I use dot symbol '.' as separator
for sentence in variable_with_original_text.split('.'):
    # And append sentence to the list
    text_list.append(sentence)

# I create two variables: one for transformed text and another one for the last sentence that will be created by adding
# of last words of each sentence
final_text = ''
last_sentence = ''

# In this for... statement I perform all transformation operations, also, I create last sentence here.
# Just as reminder: I work separately with each sentence
for i in range(len(text_list)-1):
    # Firstly I replace all line feeds by space by .replace() method.
    text_list[i] = text_list[i].replace('\n', ' ')
    # Then I delete all spaces at the beginning and the end of the sentence by method .strip().
    text_list[i] = text_list[i].strip()
    # Then I transform all letters to lowercase by .lower() method.
    text_list[i] = text_list[i].lower()
    # Finally I transform first letter of the sentence to uppercase by method .capitalize().
    text_list[i] = text_list[i].capitalize()
    # Then I correct expression 'iz' to 'is' by replacing method .sub() from library re. I do not use any regex
    # patterns here because there is actually no need in that case. All misspelling happens in independent expressions,
    # not in the words (i.e. word like 'existing'). That's why I use only spaces to avoid replacing in the words like
    # 'normalize'.
    text_list[i] = re.sub(' iz ', ' is ', text_list[i])
    # I decide to replace also "iz" expression in the sentence 'fix“iZ” with correct “is”...' because I assume that
    # this expression is also incorrect. I do not combine replacement from line 51 and line 59 to one pattern because
    # of the next reason: I may create pattern like '\Wiz\W$' or '[^a-zA-Z0-9_]iz[^a-zA-Z0-9_]$'. That pattern
    # catch both 'iz' and '“iz”' expression, but in that case I need to understand what exactly pattern catch.
    # I can do it by if... elif... statements, but I think that for that case it will be code complication.
    # That's why I just wrote two lines which work only in a specific case instead of block of code that will work in
    # mostly cases.
    text_list[i] = re.sub('“iz”', ' “is” ', text_list[i])
    # I also notice that we have 'tex.' expression in the end of the sentence 'last iz TO calculate nuMber
    # OF Whitespace characteRS in this Tex.' I also decide to replace it by word 'text'. In this small pattern I use
    # end of the line character '$' to make sure that I not replace words that start from 'tex'. I also should use
    # end of the line character '^' to make sure that I not replace words that end to 'tex', but fortunately we don't
    # have such words in the original text. That's why I don't use this character
    text_list[i] = re.sub(r'tex$', 'text', text_list[i])
    # Then I replace all double, triple and more whitespaces between words to one whitespace
    text_list[i] = re.sub(r'\s+', ' ', text_list[i])
    # Then I split each words to three variables. Variable 'first' contains first word of the sentence. Variable 'last'
    # contains the last word of the sentence. Variable (or it is better to say array or *args) '*middle' contains all
    # other words (we can say words that is not first and last in the sentence). We will work with 'last'
    # and 'middle' variables only.
    first, *middle, last = text_list[i].split()
    # In the task requirements we need to create last sentence with last words. I assume that I need to use only words.
    # We have one sentence with the number in the end of the sentence. In that case we should take word before it.
    # To check if last expression of the sentence is number we can use method .isdigit().
    if not last.isdigit():
        # If the last expression is not a digit then we just add it to our variable 'last_sentence' with a space
        last_sentence += last + ' '
    else:
        # If the last expression is digit then we take penultimate expression from the sentence and add it to our
        # variable 'last_sentence' with a space. We should also check if the penultimate expression is digit but in
        # that case it also will be code complication (because we have explicit text and assuming that we don't have
        # any new text), so I decide not to check this.
        last_sentence += middle[-1] + ' '
    # After all operations of original text transforming we add dot to each sentence, because we lost it when parsed
    # original text
    final_text += text_list[i] + '. '

# We still need to perform some operation with the last sentence. Firstly I delete all spaces from the start and the end
# of the sentence
last_sentence = last_sentence.strip()
# Then I transform each letter of the sentect to lowecase
last_sentence = last_sentence.lower()
# Then I transform first letter of the sentence to uppercase
last_sentence = last_sentence.capitalize()
# Finally I add a dot to the end of the sentence
last_sentence += '.'

# After all transformations we can concat our result
final_text = final_text + last_sentence

# And print it
print('\nTransformed text with added sentence:\n\n', final_text)

# Also we need to count all whitespaces in the original text. To do this I use unicode combination that represents
# whitespace symbol. Unfortunately, I count only 84 symbols. I also tried another unicode combinations with property
# of whitespace (you can find list of unicode combinations here: http://xahlee.info/comp/unicode_whitespace.html) but
# almost all of them returns 0, except of lines count. Maybe I incorrectly paste the original text, but for now,
# I don't know any solutions to count 87 whitespaces
print('\nNumber of whitespaces from original text:', variable_with_original_text.count('\u0020'))
