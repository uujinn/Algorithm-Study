from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs, key = lambda x : len(x))

        if len(strs) == 0:
            return ""
        
        for idx, char in enumerate(shortest):       # index, shortest의 각 char
            for str in strs:
                if str[idx] != char:
                    return shortest[:idx]
        return shortest

strs = ["flower","flow","flight"]
print(Solution().longestCommonPrefix(strs))

# https://leetcode.com/problems/longest-common-prefix/