def solution(s):
    length = []
    result = ""

    if len(s) == 1:
        return 1

    for cut in range(1, (len(s) // 2) + 1):
        count = 1
        temp = s[:cut]
        for i in range(cut, len(s), cut):
            if s[i:i + cut] == temp:
                count += 1
            else:
                if count == 1:
                    count = ""
                result += str(count) + temp
                temp = s[i:i + cut]
                count = 1

        if count == 1:
            count = ""
        result += str(count) + temp
        length.append(len(result))
        result = ""

    return min(length)