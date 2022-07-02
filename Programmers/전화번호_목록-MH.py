def solution(phone_book):
    phone_book.sort()
    
    for i in range(len(phone_book) - 1):
        pb = phone_book[i]
        if pb == (phone_book[i + 1])[:len(pb)]:
            return False
                
    return True

print(solution(["119", "97674223", "1195524421"]))