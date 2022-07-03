from collections import defaultdict
from itertools import combinations


def solution(phone_book):
    phone_dict = defaultdict()

    for p in phone_book:
        phone_dict[phone_dict] = 1
    return True


print(solution(["119", "97674223", "1195524421"]))
