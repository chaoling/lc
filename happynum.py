'''
202. Happy Number
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:

Input: n = 2
Output: false
 

Constraints:

1 <= n <= 231 - 1
'''
class Solution:
    def isHappy(self, n: int) -> bool:
        '''
        1. how to determine a cycle? if a number has been seen before that is not a 1
        e.g: n = 2: 2^2 = 4, ->16->37->9+49=58->25+64=89->64+81=145->1+16+25=42->16+4=20->4->16->....
        '''
        def op(n: int)->int:
            sum = 0
            while n:
                digit = n%10
                sum += digit ** 2
                n = n // 10
            return sum

        seen = set()
        result = 0
        while n != 1:
            n = op(n)
            if n not in seen:
                seen.add(n)
            else:
                return False
        return True

if __name__ == "__main__":
    sol = Solution()
    print(sol.isHappy(19))  # Output: True
    print(sol.isHappy(2))   # Output: False
    print(sol.isHappy(1))   # Output: True
    print(sol.isHappy(7))   # Output: True