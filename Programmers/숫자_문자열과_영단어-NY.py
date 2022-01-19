def solution(s):
    num_dic = {"one": "1", "two":"2", "three":"3", "four":"4",
               "five":"5", "six":"6", "seven":"7", "eight":"8",
               "nine":"9", "zero":"0"}
    for string, num in num_dic.items():
        if string in s:
            s = s.replace(string, num)
    return int(s)