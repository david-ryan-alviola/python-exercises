# data_types_and_variables

# You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know yet if they're going to like it). If price for a movie per day is 3 dollars, how much will you have to pay?

days_movies_rented = [3, 5, 1]
price_per_day = 3

total_per_movie = [(n * price_per_day) for n in days_movies_rented]
sum(total_per_movie)
# 27

# Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. How much will you receive in payment for this week? You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.

places_worked = [{"pay_rate" : 400, "hours_worked" : 6},
    {"pay_rate" : 380, "hours_worked" : 4},
    {"pay_rate" : 350, "hours_worked" : 10}]

total_per_job = [(place["pay_rate"] * place["hours_worked"]) for place in places_worked]

sum(total_per_job)
# 7680

# A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.

class_is_full = False
class_has_conflict_with_schedule = False

can_enroll = not class_is_full and not class_has_conflict_with_schedule
can_enroll

# A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.

is_premium_member = False
has_more_than_two_items = True
offer_is_expired = False

offer_applies = not offer_is_expired and (is_premium_member or has_more_than_two_items)
offer_applies

# Create a variable that holds a boolean value for each of the following conditions:

# the password must be at least 5 characters
# the username must be no more than 20 characters
# the password must not be the same as the username
# bonus neither the username or password can start or end with whitespace

username = 'codeup'
password = 'notastrongpassword'

password_is_at_least_5_chars = len(password) >= 5
username_is_less_than_21_chars = len(username) <= 20
password_is_same_as_username = username == password
password_starts_or_ends_with_whitespace = username.startswith(" ") or username.endswith(" ")
username_starts_or_ends_with_whitespace = password.startswith(" ") or password.endswith(" ")

username_is_valid = username_is_less_than_21_chars and not username_starts_or_ends_with_whitespace
password_is_valid = password_is_at_least_5_chars and not password_is_same_as_username and not password_starts_or_ends_with_whitespace

password_and_username_are_valid = username_is_valid and password_is_valid
password_and_username_are_valid