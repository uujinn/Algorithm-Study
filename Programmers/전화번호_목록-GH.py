def solution(phone_book):
    answer = True
    dict = {}

    for i in phone_book:
        dict[i] = 1

    for number in phone_book:
        temp = ''
        for num in number:
            temp += num
            if temp in dict and temp != number:
                answer = False

    return answer