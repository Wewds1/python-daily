"""
Markdown Heading Converter
Given a string representing a Markdown heading, return the equivalent HTML heading.

A valid Markdown heading must:

Start with zero or more spaces, followed by
1 to 6 hash characters (#) in a row, then
At least one space. And finally,
The heading text.
The number of hash symbols determines the heading level. For example, one hash symbol corresponds to an h1 tag, and six hash symbols correspond to an h6 tag.

If the given string doesn't have the exact format above, return "Invalid format".

For example, given "# My level 1 heading", return "<h1>My level 1 heading</h1>".

Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included.
"""


def convert(heading):
    h = heading.rstrip()

    i = 0
    while i < len(h) and h[i] == " ":
        i += 1

    if i == len(h):
        return "Invalid format"

    count_hash = 0
    while i < len(h) and h[i] == "#":
        count_hash += 1
        i += 1

    if count_hash == 0 or count_hash > 6:
        return "Invalid format"

    if i == len(h) or h[i] != " ":
        return "Invalid format"

    text = h[i:].strip()
    if len(text) == 0:
        return "Invalid format"

    return f"<h{count_hash}>{text}</h{count_hash}>"
