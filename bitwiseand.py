'''
Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.
201. Bitwise AND of Numbers Range

Example 1:

Input: left = 5, right = 7
Output: 4
Example 2:

Input: left = 0, right = 0
Output: 0
Example 3:

Input: left = 1, right = 2147483647
Output: 0
 

Constraints:

0 <= left <= right <= 231 - 1
'''
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        '''
        from a->b, bitwise and will make all lower bits zero depends on the range
        if only 1, then bit -1 is zero, if 2, then bit -1 and -2 is zero, if 2n, then
        bit log(2n) is zero
        '''
        delta = right - left
        if delta == 0:
            return left
        diff = left ^ right
        shift = diff.bit_length()
        return left & ~((1 << shift) - 1) # clear bits
    
    def rangeBitwiseAnd2(self, left: int, right: int) -> int:
        '''
        Shift left and right rightwards until they are equal, keeping track of how many shifts you did. This finds the common prefix of left and right. Then shift back.
        '''
        shift = 0
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift

if __name__ == "__main__":
    s = Solution()
    print(s.rangeBitwiseAnd(5,7)) # 4
    print(s.rangeBitwiseAnd(0,1)) # 0
    print(s.rangeBitwiseAnd(1,2147483647)) # 0
    print(s.rangeBitwiseAnd(600000000,2147483647)) # 536870912
    print(s.rangeBitwiseAnd(10,11)) # 10
    print(s.rangeBitwiseAnd(11,12)) # 8
    print(s.rangeBitwiseAnd(12,15)) # 12
    print(s.rangeBitwiseAnd(26,30)) # 24
    print(s.rangeBitwiseAnd(26,31)) # 24
    print(s.rangeBitwiseAnd(26,32)) # 0
