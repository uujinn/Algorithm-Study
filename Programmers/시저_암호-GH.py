import string

def soultion(s, n):
    result = ""
    base = ""

    for c in s:
        if c in string.ascii_lowercase:
            base = string.ascii_lowercase
        elif c in string.ascii_uppercase:
            base = string.ascii_uppercase
        else:
            result += c
            continue
        a = base.index(c) + n
        result += base[a % len(base)]

    return result