def solution(s):
    answer = 0
    result = []

    if len(s) == 1:
        return 1

    for i in range(1, len(s)//2 + 1):  # 절반만 하면됨
        arr = ""
        cnt = 1
        sliced = s[:i]

        for j in range(i, len(s), i):
            if s[j:i+j] == sliced:
                cnt += 1
            else:

                if cnt == 1:
                    arr += sliced
                    sliced = s[j:i+j]
                else:
                    arr += str(cnt) + sliced
                    sliced = s[j:i+j]
                    cnt = 1

        if cnt == 1:
            arr += sliced
        else:
            arr += str(cnt) + sliced
        result.append(len(arr))

    answer = min(result)

    return answer
