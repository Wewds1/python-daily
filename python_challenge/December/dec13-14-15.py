#DECEMBER 15 challenge
def speed_check(speed_mph, speed_limit_kph):

    km = speed_mph * 1.60934
    if km <= speed_limit_kph:
        return "Not Speeding"
    elif abs(speed_limit_kph - km) <= 5:
        return "Warning"
    elif 5 < abs(speed_limit_kph - km):
        return "Ticket"

print(speed_check(40, 60))
"""
Given the speed you are traveling in miles per hour (MPH), and a speed limit in kilometers per hour (KPH), determine whether you are speeding and if you will get a warning or a ticket.

1 mile equals 1.60934 kilometers.
If you are travelling less than or equal to the speed limit, return "Not Speeding".
If you are travelling 5 KPH or less over the speed limit, return "Warning".
If you are travelling more than 5 KPH over the speed limit, return "Ticket".


Passed:1. speed_check(30, 70) should return "Not Speeding".
Passed:2. speed_check(40, 60) should return "Warning".
Passed:3. speed_check(40, 65) should return "Not Speeding".
Passed:4. speed_check(60, 90) should return "Ticket".
Passed:5. speed_check(65, 100) should return "Warning".
Passed:6. speed_check(88, 40) should return "Ticket".
"""



# DECEMBER 14 challenge

def title_case(title):

    return title.title()

# i decedied to use this cause why not its built in



"""
Capitalize It
Given a string title, return a new string formatted in title case using the following rules:

Capitalize the first letter of each word.
Make all other letters in each word lowercase.
Words are always separated by a single space.

Passed:1. title_case("hello world") should return "Hello World".
Passed:2. title_case("the quick brown fox") should return "The Quick Brown Fox".
Passed:3. title_case("JAVASCRIPT AND PYTHON") should return "Javascript And Python".
Passed:4. title_case("AvOcAdO tOAst fOr brEAkfAst") should return "Avocado Toast For Breakfast".
"""



# DECEMBER 13 challenge