# list_comprehension_practice

# 17 list comprehension problems in python

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]

# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())
    
# Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable named uppercased_fruits to hold the output of the list comprehension.
# Output should be ['MANGO', 'KIWI', etc...]
uppercased_fruits = [fruit.upper() for fruit in fruits]
uppercased_fruits

# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]
capitalized_fruits = [fruit.capitalize() for fruit in fruits]
capitalized_fruits

# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.
def has_more_than_two_vowels(word):
    vowel_count = 0
    vowels = ["a", "e", "i", "o", "u"]
    letters = [letter for letter in word]
    
    for letter in letters:
        if(letter in vowels):
            vowel_count += 1
    
    if (vowel_count > 2):
        return True
    else:
        return False

fruits_with_more_than_two_vowels = [fruit for fruit in fruits if has_more_than_two_vowels(fruit)]
fruits_with_more_than_two_vowels

# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']
def has_only_two_vowels(word):
    vowel_count = 0
    vowels = ["a", "e", "i", "o", "u"]
    letters = [letter for letter in word]
    
    for letter in letters:
        if(letter in vowels):
            vowel_count += 1
    
    if (vowel_count == 2):
        return True
    else:
        return False

fruits_with_only_two_vowels = [fruit for fruit in fruits if has_only_two_vowels(fruit)]
fruits_with_only_two_vowels

# Exercise 5 - make a list that contains each fruit with more than 5 characters
fruits_with_more_than_five_chars = [fruit for fruit in fruits if len(fruit) > 5]
fruits_with_more_than_five_chars

# Exercise 6 - make a list that contains each fruit with exactly 5 characters
fruits_with_only_five_chars = [fruit for fruit in fruits if len(fruit) == 5]
fruits_with_only_five_chars

# Exercise 7 - Make a list that contains fruits that have less than 5 characters
fruits_with_less_than_five_chars = [fruit for fruit in fruits if len(fruit) < 5]
fruits_with_less_than_five_chars

# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]
fruit_name_lengths = [len(fruit) for fruit in fruits]
fruit_name_lengths

# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"
fruits_with_letter_a = [fruit for fruit in fruits if fruit.find("a") > -1]
fruits_with_letter_a

# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 
even_numbers = [number for number in numbers if number % 2 == 0]
even_numbers

# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers
odd_numbers = [number for number in numbers if number % 2 != 0]
odd_numbers

# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers
positive_numbers = [num for num in numbers if num > 0]
positive_numbers

# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers
negative_numbers = [n for n in numbers if n < 0]
negative_numbers

# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals
divisible_by_five = [n for n in numbers if n % 5 == 0]
divisible_by_five

# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]
numbers_squared = [n ** 2 for n in numbers]
numbers_squared

# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.
odd_negative_numbers = [n for n in numbers if n < 0 and n % 2 != 0]
odd_negative_numbers

# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. 
numbers_plus_5 = [n + 5 for n in numbers]
numbers_plus_5

# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list. *Hint* you may want to make or find a helper function that determines if a given number is prime or not.
def is_prime_num(num):
    if (num < 0):
        return False
        
    is_prime = True
    
    for n in range(num):
        if (n == 0 or n == 1):
            continue
        if (num % n == 0 and num != n):
            is_prime = False
    
    return is_prime

primes = [n for n in numbers if is_prime_num(n)]
primes
