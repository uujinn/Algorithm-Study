class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        answer = ""
        strs = sorted(strs)

        if len(strs) == 0:
            return ""

        for c in strs[0]:
            if strs[-1].startswith(answer + c): # prefix = 문자열 첫번째 캐릭터부터 하나씩 추가
                answer += c
            else:
                break
        return answer

