def solution(s):
    num_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for num in num_list:
        s = s.replace(num, str(num_list.index(num)))

    return int(s)
