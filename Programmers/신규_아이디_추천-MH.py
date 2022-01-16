def commaTrim(str):
    trim_str = list(str)
    
    if (len(trim_str) <= 1):
        if (trim_str == '.'):
            return ''
        else:
            return trim_str
        
    while (len(trim_str) > 1):
        if (trim_str[0] == '.'):
            trim_str[0] = ''
        if (trim_str[-1] == '.'):
            trim_str[-1] = ''
            
        if not (trim_str[0] == '.' and trim_str[len(trim_str) - 1] == '.'):
            break
        
        trim_str = [i for i in trim_str if i]
   
    return trim_str

def solution(new_id):
    # 1단계
    answer = list(new_id.lower())
    
    # 2단계
    for i in range(len(answer)):
        char = answer[i]
        if not (char.isalnum() or char == '-' or char == '_' or char == '.'):
            answer[i] = ""
    
    answer = [i for i in answer if i]   # 리스트 내 공백 제거
    
    # 3단계
    split_str = "".join(answer)          # list to str
    split_str = split_str.split('.')
    split_str = [i for i in split_str if i]
    answer = '.'.join(split_str)
    
    # 4단계
    answer = commaTrim(answer)
        
    # 5단계
    if (len(answer) == 0):
        answer = 'a'
    
    # 6단계
    if (len(answer) >= 16):
        answer = answer[:15]
    answer = commaTrim(answer)
    
    # 7단계
    while (len(answer) < 3):
        char = answer[-1]
        answer.append(char)
    
    answer = "".join(answer)          # list to str
    
    return answer


id1 = '...!@BaT#*..y.abcdefgh.ijklm..'
id2 = 'z-+.^.'
id3 = '=.='
id4 = '123_.def'
id5 = 'abcdefghijklmn.p'

print(solution('...!@BaT#*..y.abcdefgh.ijklm..'))