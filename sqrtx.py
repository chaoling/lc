'''
69. Sqrt(x)
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
 

Constraints:

0 <= x <= 2**31 - 1    
'''
class Solution:
    def mySqrt(self, x: int) -> int:
        '''
        can we use guess and check? there is also some existing algorithms to get the square root
        of the number, such as newton's method?
        can we use binary search to narrow down it quicker?
        '''
        left, right = 0, x
        while left <= right:
            mid = left + (right-left) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1
        return left - 1

    def mySqrt2(self, x: int) -> int:
        '''
        Newton's method
        '''
        if x == 0:
            return 0
        r = x
        while r * r > x:
            r = (r + x // r) // 2
        return r

if __name__ == "__main__":
    s = Solution()
    print(s.mySqrt(8))
    print(s.mySqrt2(8))
    print(s.mySqrt(4))
    print(s.mySqrt2(4))
    print(s.mySqrt(0))
    print(s.mySqrt2(0))