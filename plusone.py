'''

'''
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        '''
        this is just like adding 1 with carry
        '''
        class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        '''
        this is just like adding 1 with carry
        '''
        carry = 1
        for i in range(-1,-1-len(digits),-1):
            digits[i] = digits[i] + carry
            carry = digits[i] // 10
            digits[i] %= 10
            if carry == 0:
                break
                
        return digits if carry == 0 else [carry]+digits
    def plusOne2(self, digits: List[int]) -> List[int]:
        '''
        convert to int, add 1, convert back to list
        '''
        num = 0
        for d in digits:
            num = num * 10 + d
        num += 1
        return [int(d) for d in str(num)]
    def plusOne3(self, digits: List[int]) -> List[int]:
        '''
        pythonic
        '''
        return [int(d) for d in str(int(''.join(map(str, digits))) + 1)]
if __name__ == "__main__":
    a = Solution()
    print(a.plusOne([1,2,3]))
    print(a.plusOne([4,3,2,1]))
    print(a.plusOne([9]))
    print(a.plusOne([9,9,9]))