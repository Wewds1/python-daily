"""
Given a string date in the format YYYY-MM-DD, return the day of the week.

Valid return days are:

"Sunday"
"Monday"
"Tuesday"
"Wednesday"
"Thursday"
"Friday"
"Saturday"
Be sure to ignore time zones.
"""


from datetime import datetime

def get_weekday(date_string):

    date = datetime.strptime(date_string, '%Y-%m-%d')

    return date.strftime('%A')


print(get_weekday('2025-11-06'))