def solution(s):
    nums = s.split('{')
    temp_arr = []
    answer = []
    for n in nums:
        if n=='': continue
        else: temp_str = n[:-2]
        temp = temp_str.split(',')
        temp_arr.append(temp)
    temp_arr.sort(key=len)
    for temp in temp_arr:
        for t in temp:
            if int(t) in answer: continue
            else: answer.append(int(t))
        
    return answer