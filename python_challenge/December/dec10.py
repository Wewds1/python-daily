"""
Markdown Bold Parser
Given a string that may include some bold text in Markdown, return the equivalent HTML string.

Bold text in Markdown is any text that starts and ends with two asterisks (**) or two underscores (__).
There cannot be any spaces between the text and the asterisks or underscores, but there can be spaces in the text itself.
Convert all bold occurrences to HTML b tags and return the string.
For example, given "**This is bold**", return "<b>This is bold</b>".

Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included.
"""

import re
def parse_bold(markdown):

            
    markdown = re.sub(r"\*\*(\S.+?\S)\*\*", r'<b>\1</b>', markdown)

    markdown = re.sub(r"__(\S.+?\S)__", r"<b>\1</b>", markdown)

    return markdown

print(parse_bold("**This is not bold **"))
print(parse_bold("**This is bold**"))
