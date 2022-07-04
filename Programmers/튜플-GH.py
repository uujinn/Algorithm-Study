import re


def solution(s):
    answer = []
    list = re.findall('\d+(?:\,\d+)*', s)
    list = sorted(list, key=len)

    for i in list:
        for num in i.split(','):
            if int(num) not in answer:
                answer.append(int(num))
    return answer