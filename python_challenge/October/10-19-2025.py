"""
Given a string of a valid HTML element, return the attributes of the element using the following criteria:

You will only be given one element.
Attributes will be in the format: attribute="value".
Return an array of strings with each attribute property and value, 
separated by a comma, in this format: ["attribute1, value1", "attribute2, value2"].
Return attributes in the order they are given.
If no attributes are found, return an empty array.

"""

# I give up on this one, let ai help me by importing re. this is beyond my current abilities.


import re
def extract_attributes(element):

    pairs = re.findall(r'([^\s=]+)\s*=\s*"([^"]*)"', element)
    return [f"{name}, {value}" for name, value in pairs]