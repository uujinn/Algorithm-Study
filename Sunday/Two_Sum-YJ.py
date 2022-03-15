from typing import List
class Solution:

    def plusOne(self, digits):
        
        for i in reversed(range(len(digits))): # 계산하기 위해 뒤에서 부터 확인
            if digits[i] < 9:
                digits[i] += 1
                return digits

            else:
                digits[i] = 0
        
        digits.insert(0, 1) # 자리수 바뀌면 맨 앞에 1 넣어줌

        return digits

s = Solution()
print(s.plusOne([1,9]))