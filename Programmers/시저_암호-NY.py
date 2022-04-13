def solution(string,n):
    asc = ""
    for s in string:
        ord_s = ord(s)
        if ord_s == 32: 
            asc += s
            continue
        elif ord_s in range(65, 91):
            ord_s += n
            ord_s -= 26 if ord_s >= 91 else 0
        else:
            ord_s += n
            ord_s -= 26 if ord_s >= 123 else 0
        asc += chr(ord_s)
    return asc