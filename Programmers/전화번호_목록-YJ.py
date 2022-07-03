from itertools import combinations


def solution(phone_book):

    phone_book.sort()
    for comb in combinations(phone_book, 2):
        p1, p2 = comb
        if p2.startswith(p1):
            return False
    return True


print(solution(["119", "97674223", "1195524421"]))
