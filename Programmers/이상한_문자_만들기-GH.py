def solution(s):
    arr = []

    for str in s.split(' '):
        cnt = 0

        for i in str:
            if cnt % 2 == 0:
                arr.append(i.upper())
            else:
                arr.append(i.lower())
            cnt += 1

        arr.append(" ")

    return "".join(arr[:-1])
