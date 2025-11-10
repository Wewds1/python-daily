"""

Extension Extractor
Given a string representing a filename, return the extension of the file.

The extension is the part of the filename that comes after the last period (.).
If the filename does not contain a period or ends with a period, return "none".
The extension should be returned as-is, preserving case.
"""

def get_extension(filename):
    parts = filename.split('.')
    if len(parts) == 1 or parts[-1] == "":
        return "none"
    else:
        return parts[-1]
    # if filename.count('.') < 1:
    #     return 'none'
    # if filename.split(".")[-1]:
    #     return filename.split(".")[-1]
    # else:
    #     return 'none'
print(get_extension("README"))



