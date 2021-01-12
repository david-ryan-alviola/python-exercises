# data types, operators, and variables

# Identify the data type of the following values:

type(99.9) #float
type("False") #str
type(False) #bool
type('0') #str
type(0) #int
type(True) #bool
type('True') #str
type([{}]) #list
type({'a':[]}) #dict

# What data type would best represent:

# A term or phrase typed into a search box? str
# If a user is logged in? bool
# A discount amount to apply to a user's shopping cart? float
# Whether or not a coupon code is valid? bool
# An email address typed into a registration form? str
# The price of a product? float
# A Matrix? dict
# The email addresses collected from a registration form? list of str
# Information about applicants to Codeup's data science program? str or clob?

# For each of the following code blocks, read the expression and predict what the result of evaluating it would be, then execute the expression in your Python REPL.

# error 
'1' + 2

# 2
6 % 4

# int
type(6 % 2)

# str
type(type(6 % 2)) # type

# error
'3 + 4 is ' + 3 + 4

# False
0 < 0

# False
'False' == False

# False
True == 'True'

# True
5 >= -5

# True
!False or False # nothing is returned but `not False or False` returns True

# True
True or 42

# False
!True && !False # nothing is returned but `not True and not False` return False

# 1
6 % 5

# False
5 < 4 and 1 == 1

# False
'codeup' == 'codeup' and 'codeup' == 'Codeup'

# Error
4 >= and 1 !== '1'

# True
6 % 3 == 0

# True
5 % 2 != 0

# Error
[1] + 2

# [1,2]
[1] + [2]

# 2
[1] * 2 # [1, 1]

# [2]
[1] * [2] # error

# False
[] + [] == [] # True

# Error
{} + {}