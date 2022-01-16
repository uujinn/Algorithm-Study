class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        shortest = min(strs, key=len)
        for i, s in enumerate(shortest):
            for str in strs:
                if str[i] != s:
                    return shortest[:i]
                
        return shortest

#LeetCode: https://leetcode.com/problems/longest-common-prefix/