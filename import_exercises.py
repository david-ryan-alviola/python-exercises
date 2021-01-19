#!/usr/bin/env python
# coding: utf-8

# ### Import and test 3 of the functions from your functions exercise file.
# * Import each function in a different way:
#     1. import the module and refer to the function with the . syntax
#     2. use from to import the function directly
#     3. use from and give the function a different name

# In[89]:


import functions_exercises
from functions_exercises import normalize_name
from functions_exercises import is_consonant as determine_consonant

assert functions_exercises.is_two("2")
assert normalize_name("First Name") == "first_name"
assert determine_consonant("z")


# ### How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?

# In[24]:


from itertools import product

num_of_combos = len(list(product("abc", "123")))
print(f"{num_of_combos} combinations")


# ### How many different ways can you combine two of the letters from "abcd"?

# In[28]:


from itertools import combinations as combo

num_of_combos = len(list(combo("abcd", 2)))
print(f"{num_of_combos} combinations")


# ### Use the load function from the json module to open this file, it will produce a list of dictionaries. Using this data, write some code that calculates and outputs the following information:

# In[88]:


import json

profiles = open("profiles.json")
list_of_profiles = json.load(profiles)
list_of_profiles


# In[87]:


list_of_profiles[0]
len(list_of_profiles)


# In[79]:


# 1. Total number of users
total_users = len(list_of_profiles)
total_users


# In[44]:


# 2. Number of active users
active_users = len([user for user in list_of_profiles if user["isActive"]])
active_users


# In[46]:


# 3. Number of inactive users
inactive_users = len([user for user in list_of_profiles if not user["isActive"]])
inactive_users

assert total_users == active_users + inactive_users


# In[52]:


# 4. Grand total of balances for all users
def convert_balances_to_float(balances):
    float_list = []
    
    for balance in balances:
        balance = balance.replace("$", "")
        balance = functions_exercises.handle_commas(balance)
        float_list.append(float(balance))
    
    return float_list
    
float_balances = convert_balances_to_float([user["balance"] for user in list_of_profiles])
total_balance = sum(float_balances)

print(total_balance)


# In[92]:


# 5. Average balance per user
average_balance = total_balance / total_users
print(round(average_balance, 2))


# In[93]:


# 6. User with the lowest balance
lowest_balance = min(float_balances)
low_balance_index = float_balances.index(lowest_balance)

low_balance_user = list_of_profiles[low_balance_index]
print("User:  {}; Balance:  {}".format(low_balance_user["name"], low_balance_user["balance"]))


# In[94]:


# 7. User with the highest balance
highest_balance = max(float_balances)
high_balance_index = float_balances.index(highest_balance)

high_balance_user = list_of_profiles[high_balance_index]
print("User:  {}; Balance:  {}".format(high_balance_user["name"], high_balance_user["balance"]))


# In[95]:


# 8. Most common favorite fruit
favorite_fruits = {}

for fruit in [user["favoriteFruit"] for user in list_of_profiles]:
    if(fruit in favorite_fruits):
        favorite_fruits[fruit] += 1
    else:
        favorite_fruits[fruit] = 1

most_common_favorite_fruit = max(favorite_fruits)
most_common_favorite_fruit


# In[77]:


# 9. Least most common favorite fruit
least_common_favorite_fruit = min(favorite_fruits)
least_common_favorite_fruit


# In[99]:


# 10. Total number of unread messages for all users
def extract_digits(s):
    return "".join([c for c in s if c.isnumeric()])

unread_message_count = [extract_digits(user["greeting"]) for user in list_of_profiles]

sum([int(message) for message in unread_message_count])

