# To fulfill list with random numbers we should create this random numbers. In that case library random can help us.
# That's why I import random library before starting to work
import random


# Home task №1 - create list of 100 random numbers from 0 to 1000

# Before we can add any variables to the list, we should create this list
random_numbers_list = []

# I use for... statement with range function to fulfill list with 100 random numbers.
for i in range(100):
    # To add numbers to the list I use method .append(). This method adds element to the end of the list.
    # To generate random numbers I use method .randint() of the library random. This method creates random integer numbers.
    random_numbers_list.append(random.randint(0, 1000))

# Let's print our list
print(random_numbers_list, '\n')


# Home task №2 - sort list from min to max (without using sort())

# To sort list I use bubble sort algorithm. This algorithm takes first element and compare it with second.
# If second element is greater than the second, then they switch position between each other. This operation performs
# for each element.
# I use two for... statements to make sure that all elements are sorted correctly. As for range() method value I take
# length of the list by len() method. In that case even if the biggest element will be at the 1 position,
# in the end of the sorting that element will be at the last position
for j in range(len(random_numbers_list)):
    # In this for... statement I take value-1 for range() method because I want to access element with position
    # in the list +1. If I not perform -1 operation then I will get error: list index if out of the range
    for i in range(len(random_numbers_list) - 1):
        # In the line 31 I compare first element with the next one. If first element is greater than the next one, then
        # we perform next operations.
        if random_numbers_list[i] > random_numbers_list[i+1]:
            # in this section we swap elements by the help of the temporary variable
            temporary_variable = random_numbers_list[i]
            random_numbers_list[i] = random_numbers_list[i+1]
            random_numbers_list[i+1] = temporary_variable

# Let's print our sorted list
print(random_numbers_list, '\n')


# Home task №3 - calculate average for even and odd numbers

# To calculate average we need to know next two variables: the sum of elements and number of elements.
# Let's create both variables for each odd and even numbers
sum_for_odd = 0
sum_for_even = 0
count_for_odd = 0
count_for_even = 0

# To understand which number is odd and which is even we need to parse list by for... statement.
for i in range(len(random_numbers_list)):
    # This statement checks if number is even. '%' operator returns the fractional part of the division by 2.
    # If this part == 0, then this number is even. Else - odd. I and this program count 0 as even.
    if random_numbers_list[i] % 2 == 0:
        # I use += operator to simplify code.
        # In other case I should write sum_for_even = sum_for_even + random_numbers_list[i]
        sum_for_even += random_numbers_list[i]
        # Same as for line 61, but in this case for counter
        count_for_even += 1
    else:
        # Same as for line 61, but in this case for odd number
        sum_for_odd += random_numbers_list[i]
        # Same as for line 63, but in this case for odd number
        count_for_odd += 1

# Let's calculate average
average_for_even = sum_for_even / count_for_even
average_for_odds = sum_for_odd / count_for_odd


# Home task 4 - print both average result in console

# To print result I use print() method. 'f' before the quotes enable us to use variables in the {}
# without closing this quotes. Also, I round result to 2 digits after comma by round() method
print(f"Average for even numbers: {round(average_for_even,2)}; Average for odd numbers: {round(average_for_odds,2)}")
