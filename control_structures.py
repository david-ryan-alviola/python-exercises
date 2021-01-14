#!/usr/bin/env python
# coding: utf-8

# ## Prompt the user for a day of the week, print out whether the day is Monday or not.

# In[2]:


day_of_the_week = input("Please enter the current day of the week:  ")

if (day_of_the_week.lower() == "monday"):
    print("Sorry. It is Monday.")
else:
    print("Aren't you glad it's not Monday?")


# ## Prompt the user for a day of the week, print out whether the day is a weekday or a weekend

# In[3]:


day_of_the_week = input("Please enter the current day of the week:  ")
weekend_days = ["saturday", "sunday"]

if (day_of_the_week.lower() in weekend_days):
    print("Enjoy your weekend!")
else:
    print("Work hard for that weekend!")


# ## create variables and make up values for
#     1. the number of hours worked in one week
#     2. the hourly rate
#     3. how much the week's paycheck will be
#     4. write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours
# 

# In[4]:


hours_worked_per_week = 41
hourly_rate = 100

def calculate_weekly_paycheck_amount(hours_worked_per_week, hourly_rate):
    regular_pay = hours_worked_per_week * hourly_rate
    overtime_pay = 0
    
    if(hours_worked_per_week > 40):
        overtime_hours = hours_worked_per_week - 40
        overtime_pay = overtime_hours * hourly_rate * .5
    
    return regular_pay + overtime_pay

weekly_paycheck_amount = calculate_weekly_paycheck_amount(hours_worked_per_week, hourly_rate)
print("Pay for this week:  ${:.2f}".format(weekly_paycheck_amount))


# ## While
#     1. Create an integer variable i with a value of 5.
#     2. Create a while loop that runs so long as i is less than or equal to 15
#     3. Each loop iteration, output the current value of i, then increment i by one.

# In[7]:


i = 5
while i <= 15:
    print(i)
    i += 1


#     * Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.

# In[8]:


i = 0
while i <= 100:
    print(i)
    i += 2


#     * Alter your loop to count backwards by 5's from 100 to -10.

# In[9]:


i = 100
while i >= -10:
    print(i)
    i -= 5


#     * Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000.

# In[9]:


i = 2
while i < 1_000_000:
    print(i)
#     i = i ** 2
    i **= 2 # shorthand of above code


#     * Write a loop that uses print to create the output shown below.

# In[11]:


i = 100
while i > 0:
    print(i)
    i -= 5


# ## For Loops
#     * Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.

# In[17]:


user_num = input("Please input the number you wish to multiply:  ")

for n in range(1,11):
    print("{} x {} = {}".format(n, user_num, n * int(user_num)))


#     * Create a for loop that uses print to create the output shown below.

# In[18]:


for n in range(1, 10):
    string_num = str(n)
    print(string_num * n)


# ## break and continue
#     * Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.

# In[27]:


user_num = ""

# Following directions
while True:
    user_num = input("Number to skip is:  ")
    if user_num.isdigit() and int(user_num) % 2 != 0 and int(user_num) >= 1 and int(user_num) <= 50:
        break

# Alternative solution
# while not user_num.isdigit() or (int(user_num) % 2 == 0) or (int(user_num) < 1) or (int(user_num) > 50):
#     user_num = input("Please enter an odd number between 1 and 50:  ")

print("")

for n in range(1, 51):
    if n == int(user_num):
        print(f"Yikes! Skipping number:  {n}")
        continue
    if n % 2 != 0:
        print(f"Here is an odd number:  {n}")


#     * The input function can be used to prompt for input and use that input in your python code. Prompt the user to enter a positive number and write a loop that counts from 0 to that number. (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, so you'll need to convert this to a numeric type.)

# In[30]:


user_num = ""

while not user_num.isdigit() or int(user_num) <= 0:
    user_num = input("Please enter a positive number:  ")
    
for n in range (0, int(user_num) + 1):
    print(n)


#     * Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1.

# In[35]:


user_num = ""

while not user_num.isdigit() or int(user_num) <= 0:
    user_num = input("Please enter a positive number:  ")
    
for n in reversed(range(1, int(user_num) + 1)):
    print(n)


# ## Fizzbuzz
#     1. One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.
#     2. Write a program that prints the numbers from 1 to 100.
#     3. For multiples of three print "Fizz" instead of the number
#     4. For the multiples of five print "Buzz".
#     5. For numbers which are multiples of both three and five print "FizzBuzz".

# In[5]:


for i in range(1, 101):
    output = ""
    
    if (i % 3 == 0):
        output += "Fizz"
    if (i % 5 == 0):
        output += "Buzz"
    
    if (len(output) > 0):
        print(output)
    else:
        print(i)


# ## Display a table of powers.
#     1. Prompt the user to enter an integer.
#     2. Display a table of squares and cubes from 1 to the value entered.
#     3. Ask if the user wants to continue.
#     4. Assume that the user will enter valid data.
#     5. Only continue if the user agrees to.

# In[9]:


wants_to_continue = True

while wants_to_continue:
    user_num = input("What number would you like to go up to?  ")
    num = 0
    
    if (user_num.isdigit()):
        num = int(user_num)
    else:
        continue
    
    print("")
    print("Here is your table!")
    print("")
    print("number | squared | cubed")
    print("------ | ------- | -----")
    
    for i in range (1, num + 1):
        # Look at solution for how to format properly
        print("{}      | {}       | {}".format(i, i ** 2, i ** 3))
    
    user_continue = input("Do you want to continue (y/n)?  ")
    
    if (user_continue.lower() != "y" and user_continue.lower() != "yes"):
        wants_to_continue = False
    


# ## Convert given number grades into letter grades.
#     1. Prompt the user for a numerical grade from 0 to 100.
#     2. Display the corresponding letter grade.
#     3. Prompt the user to continue.
#     4. Assume that the user will enter valid integers for the grades.
#     5. The application should only continue if the user agrees to.

# In[1]:


wants_to_continue = True

while wants_to_continue:
    grade = input("Please enter the numerical grade:  ")
    num_grade = int(grade)
    
    if (num_grade >= 88):
        print("A")
    elif (num_grade < 88 and num_grade >= 80):
        print("B")
    elif (num_grade < 80 and num_grade >= 67):
        print("C")
    elif (num_grade < 67 and num_grade >= 60):
        print("D")
    else:
        print("F")
    
    user_continue = input("Do you want to continue (y/n)?  ")
    
    if (user_continue.lower() != "y" and user_continue.lower() != "yes"):
        wants_to_continue = False


# ## Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the list should have the keys title, author, and genre. Loop through the list and print out information about each book.
#     * Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.

# In[8]:


books = [{"title" : "mystery1", "author" : "author1", "genre" : "mystery"},
         {"title" : "adventure1", "author" : "author2", "genre" : "adventure"},
         {"title" : "biography1", "author" : "author3", "genre" : "nonfiction"},
         {"title" : "mystery2", "author" : "author4", "genre" : "mystery"},
         {"title" : "adventure2", "author" : "author5", "genre" : "adventure"},
         {"title" : "biography2", "author" : "author6", "genre" : "nonfiction"},
         {"title" : "reference1", "author" : "author7", "genre" : "nonfiction"}
        ]

genre = input("Please enter the genre you wish to search for:  ")

match = False
for book in books:
        
    if book["genre"] == genre.lower():
        print(book["title"])
        match = True

if not match:
    print("No books of that genre.")


# In[ ]:




