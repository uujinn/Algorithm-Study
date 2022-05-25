def solution(s):
    length = []
    result = ""

    if len(s) == 1:
        return 1

    for C in range(1, (len(s) // 2) + 1):
        count = 1
        temp = s[:C]
        for i in range(C, len(s), C):
            if s[i:i + C] == temp:
                count += 1
            else:
                if count == 1:
                    count = ""
                result += str(count) + temp
                temp = s[i:i + C]
                count = 1

        if count == 1:
            count = ""
        result += str(count) + temp
        length.append(len(result))
        result = ""

    return min(length)