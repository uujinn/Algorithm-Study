def solution(s):
    answer = len(s)
    for i in range(len(s)//2, 0, -1):
        temp = []
        count = 0 #전체 문자열 길이
        for j in range(0, len(s)-i+1, i):
            if len(s) < j+i: temp.append(s[j:])
            else: temp.append(s[j:j+i])
        print(temp)
        for idx, t in enumerate(temp):
            if idx == 0: same = 1
            else: 
                if t == temp[idx-1]: same += 1
                else:
                    if same == 1: count += i
                    else:
                        count += len(str(same)) + i
                        same = 1
            if len(temp)-1 == idx: count += i if same == 1 else len(str(same)) + i
        print(count)
        if count < answer: answer = count
        
    return answer