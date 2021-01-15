#!/usr/bin/env python
# coding: utf-8

# ### Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

# In[42]:


def is_two(num):
    return int(num) == 2

assert is_two(2)
assert is_two(str(2))
print("Positive tests passed.")
assert is_two(4) # AssertionError expected


# ### Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

# In[43]:


vowels = ["a", "e", "i", "o", "u"]

def is_vowel(string):    
    return string.lower() in vowels

for v in vowels:
    assert is_vowel(v)

print("Positive tests passed.")
assert is_vowel("D") # AssertionError expected


# ### Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

# In[44]:


def is_consonant(string):
    return not is_vowel(string)

assert is_consonant("D")
assert is_consonant("z")
print("Positive tests passed.")
assert is_consonant("a") # AssertionError expected


# ### Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.

# In[19]:


def capitalize_consonants(word):
    if is_consonant(word[0]):
        return word.capitalize()
    else:
        return word
    
assert capitalize_consonants("chicken") == "Chicken"
assert capitalize_consonants("zebra") == "Zebra"
assert capitalize_consonants("apple") == "apple"
assert capitalize_consonants("umbrella") == "umbrella"


# ### Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

# In[23]:


def calculate_tip(tip_percent, bill_total):
    if (tip_percent < 0):
        return bill_total
    
    if (tip_percent > 1):
        tip_percent /= 100
        
    return bill_total * (tip_percent + 1)

assert calculate_tip(.5, 10) == 15
assert calculate_tip(25, 100) == 125
assert calculate_tip(-24, 24) == 24
assert calculate_tip(0, 14) == 14


# ### Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.

# In[29]:


def apply_discount(price, discount):
    discount /= 100
    
    return price * (1 - discount)

assert apply_discount(20, 50) == 10
assert apply_discount(100, 25) == 75
assert apply_discount(1, 0) == 1
assert apply_discount(5, 100) == 0


# ### Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.

# In[30]:


def handle_commas(str_num):
    return int("".join(str_num.split(",")))

assert handle_commas("1,000,000") == 1_000_000
assert handle_commas("1,000") == 1000


# ### Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).

# In[32]:


def get_letter_grade(num_grade):
    if (num_grade >= 88):
        return "A"
    elif (num_grade < 88 and num_grade >= 80):
        return "B"
    elif (num_grade < 80 and num_grade >= 67):
        return "C"
    elif (num_grade < 67 and num_grade >= 60):
        return "D"
    else:
        return "F"
        
assert get_letter_grade(88) == "A"
assert get_letter_grade(87) == "B"
assert get_letter_grade(80) == "B"
assert get_letter_grade(79) == "C"
assert get_letter_grade(67) == "C"
assert get_letter_grade(66) == "D"
assert get_letter_grade(60) == "D"
assert get_letter_grade(59) == "F"


# ### Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

# In[41]:


def remove_vowels(word):
    vowels = ["a", "e", "i", "o", "u"]
    
    trimmed_word = []
    for letter in word:
        if letter in vowels:
            continue
        trimmed_word.append(letter)
    
    return "".join(trimmed_word)

assert remove_vowels("apple") == "ppl"
assert remove_vowels("racecar") == "rccr"
assert remove_vowels("gym") == "gym"


# ### Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# 1. anything that is not a valid python identifier should be removed
# 2. leading and trailing whitespace should be removed
# 3. everything should be lowercase
# 4. spaces should be replaced with underscores
# 5. for example:
#     * Name will become name
#     * First Name will become first_name
#     * % Completed will become completed

# In[62]:


def normalize_name(name):
    special_chars_removed = []
    
    for char in name:
        if not char.isalpha():
            special_chars_removed.append(" ")
        else:
            special_chars_removed.append(char)
    
    name = "".join(special_chars_removed)
    
    formatted_name = name.lower().strip()
    formatted_name = formatted_name.replace(" ", "_")
    print(formatted_name)
    return formatted_name

assert normalize_name("Name") == "name"
assert normalize_name("First Name") == "first_name"
assert normalize_name("% Completed") == "completed"


# ### Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.

# In[67]:


def cumulative_sum(numbers):
    total = 0
    sums = []
    
    for num in numbers:
        total += num
        sums.append(total)
    
    return sums

assert cumulative_sum([1, 1, 1]) == [1, 2, 3]
assert cumulative_sum([1, 2, 3, 4]) == [1, 3, 6, 10]
assert cumulative_sum([2, 4, 6, 8]) == [2, 6, 12, 20]
assert cumulative_sum([1, 2, 3, 5, 8, 13, 21]) == [1, 3, 6, 11, 19, 32, 53]


# ### Bonus 1. Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. Bonus write a function that does the opposite.

# In[79]:


def twelveto24(twelve_hour_time):
    colons_removed = []
    
    for char in twelve_hour_time:
        if char == ":":
            colons_removed.append("")
        else:
            colons_removed.append(char)
    
    twelve_hour_time = "".join(colons_removed)
    twenty_four_hour_time = 0
    
    if (twelve_hour_time.startswith("12")):
        if (twelve_hour_time.find("am") > -1):
            twelve_hour_time = twelve_hour_time.replace("am", "")
            twenty_four_hour_time = int(twelve_hour_time) - 1200
        else:
            twelve_hour_time = twelve_hour_time.replace("pm", "")
            twenty_four_hour_time = int(twelve_hour_time)
    elif (twelve_hour_time.find("am") > -1):
        twelve_hour_time = twelve_hour_time.replace("am", "")
        twenty_four_hour_time = int(twelve_hour_time)
    else:
        twelve_hour_time = twelve_hour_time.replace("pm", "")
        twenty_four_hour_time = int(twelve_hour_time) + 1200
    
    if (twenty_four_hour_time < 1):
        twenty_four_hour_time = "0000"
    elif (twenty_four_hour_time < 10):
        twenty_four_hour_time = "000" + str(twenty_four_hour_time)
    elif (twenty_four_hour_time < 60):
        twenty_four_hour_time = "00" + str(twenty_four_hour_time)

    return str(twenty_four_hour_time)

assert twelveto24("10:45am") == "1045"
assert twelveto24("4:30pm") == "1630"
assert twelveto24("12:00am") == "0000"
assert twelveto24("12:00pm") == "1200"

