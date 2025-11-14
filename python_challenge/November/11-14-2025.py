"""
Is It the Weekend?
Given a date in the format "YYYY-MM-DD", return the number of days left until the weekend.

The weekend starts on Saturday.
If the given date is Saturday or Sunday, return "It's the weekend!".
Otherwise, return "X days until the weekend.", where X is the number of days until Saturday.
If X is 1, use "day" (singular) instead of "days" (plural).
Make sure the calculation ignores your local timezone.

"""


from datetime import datetime, timedelta

def days_until_weekend(date_string):
    date = datetime.strptime(date_string, '%Y-%m-%d').date()

    days_week = date.weekday()

    if days_week >= 5:
        return "It's the weekend!"

    days = 5 - days_week
    
    return f"{days} {'days' if days != 1 else 'day'} until the weekend."

print(days_until_weekend('2025-11-14'))