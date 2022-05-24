def solution(s):
    results = []

    for i in range(1, len(s) // 2 + 1):     # s 길이의 절반만 반복
        sliced = s[:i]
        count = 1
        temp = ''
        
        for j in range(i, len(s), i):
            # print('this : ', end='')
            # print(s[j:j + i])
            # print('sliced : ', end='')
            # print(sliced)
            
            if s[j:j + i] == sliced:
                count += 1
            else:
                if count == 1:
                    temp += sliced            
                else:
                    temp += (str(count) + sliced)

                sliced = s[j:j + i]
                count = 1
                
            # print('temp : ', end='')
            # print(temp)
            # print()
        
        # 마지막 패턴 처리
        if count == 1:
            temp += sliced
        else:
            temp += (str(count) + sliced)
                
        results.append(len(temp))
    #     print('---------------')
        
    # print(results)

    return min(results) if results else 1

print(solution("aabbaccc"))
# print(solution("abcabcabcabcdededededede"))
# print(solution("xababcdcdababcdcd"))