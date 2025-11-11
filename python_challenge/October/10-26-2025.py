"""
Duration Formatter
Given an integer number of seconds, return a string representing the same duration in the format "H:MM:SS", 
where "H" is the number of hours, "MM" is the number of minutes, and "SS" is the number of seconds. Return the time using the following rules:

Seconds: Should always be two digits.
Minutes: Should omit leading zeros when they aren't needed. Use "0" if the duration is less than one minute.
Hours: Should be included only if they're greater than zero.
"""

def format(seconds):
    hrs = seconds // 3600
    mins = (seconds % 3600) // 60
    secs = seconds % 60
    if hrs > 0:
        return f"{hrs}:{mins:02}:{secs:02}"
    else:
        return f"{mins}:{secs:02}"
    
print(format(3661))  # "1:01:01"