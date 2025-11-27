"""
What's My Age Again?
Given the date of someone's birthday in the format YYYY-MM-DD, return the person's age as of November 27th, 2025.

Assume all birthdays are valid dates before November 27th, 2025.
Return the age as an integer.
Be sure to account for whether the person has already had their birthday in 2025.
"""

from datetime import date, datetime
def calculate_age(birthday):
    day = datetime.strptime(birthday, "%Y-%m-%d").date()
    today = date.today()

    age = today.year - day.year

    if (today.month, today.day) < (day.month, day.day):
        age -= 1

    return age


print(calculate_age("2000-11-20"))