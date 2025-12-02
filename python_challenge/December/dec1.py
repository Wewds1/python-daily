"""
Camel to Snake
Given a string in camel case, return the snake case version of the string using the following rules:

The input string will contain only letters (A-Z and a-z) and will always start with a lowercase letter.
Every uppercase letter in the camel case string starts a new word.
Convert all letters to lowercase.
Separate words with an underscore (_).

"""

def to_snake(camel):
    for c in camel:
        if c.isupper():
            camel = camel.replace(f"{c}", f"_{c.lower()}")
        

    return camel

print(to_snake("helloWorld"))
print(to_snake("myVariableName"))


"""
1. to_snake("helloWorld") should return "hello_world".
Passed:2. to_snake("myVariableName") should return "my_variable_name".
Passed:3. to_snake("freecodecampDailyChallenges") should return "freecodecamp_daily_challenges".
"""