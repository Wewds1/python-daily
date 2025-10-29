"""
Given a string, determine if it is a valid email address using the following constraints:

It must contain exactly one @ symbol.
The local part (before the @):
Can only contain letters (a-z, A-Z), digits (0-9), dots (.), underscores (_), or hyphens (-).
Cannot start or end with a dot.
The domain part (after the @):
Must contain at least one dot.
Must end with a dot followed by at least two letters.
Neither the local or domain part can have two dots in a row.
"""

def validate(email):
    if email.count('@') != 1:
        return False

    local, domain = email.split('@')

    for c in local:
        if not (c.isalnum() or c in '._-'):
            return False

    if local.startswith('.') or local.endswith('.'):
        return False

    if '..' in local or '..' in domain:
        return False

    if '.' not in domain:
        return False

    dot = domain.rfind('.')
    str_dom = domain[dot+1:]
    if len(str_dom) < 2 or not str_dom.isalpha():
        return False

    return True
    