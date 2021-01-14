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

# In[52]:


def normalize_name(name):
    for char in name:
        if char.isalpha()
    formatted_name = name.lower().strip()
    formatted_name = formatted_name.replace(" ", "_")
    
    return formatted_name

assert normalize_name("Name") == "name"
assert normalize_name("First Name") == "first_name"
assert normalize_name("% Completed") == "completed"


# In[ ]:




