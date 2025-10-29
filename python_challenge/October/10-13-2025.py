"""
Given a string representing a time of the day in the 24-hour format of "HHMM", 
return the time in its equivalent 12-hour format of "H:MM AM" or "H:MM PM".

The given input will always be a four-digit string in 24-hour time format, from "0000" to "2359".

"""


def to_12_hour(time_str):
    hour = int(time_str[:2])
    minute = time_str[2:]
    if hour == 0:
        return f"12:{minute} AM"
    elif hour == 12:
        return f"12:{minute} PM"
    elif hour < 12:
        return f"{hour}:{minute} AM"
    else:
        return f"{hour - 12}:{minute} PM"