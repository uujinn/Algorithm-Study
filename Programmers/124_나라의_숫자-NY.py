dic_124 = {1: '1', 2: '2', 0: '4'}

def recur(n, answer):
    if n // 3 == 0 or n == 3:
        return dic_124[n%3]
    else:
        answer += recur(n//3 if n%3!=0 else n//3-1, answer)
        answer += dic_124[n%3]
        return answer
    
def solution(n):
    answer = ''
    return recur(n, answer)
    
print(solution(15))