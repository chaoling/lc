'''
9. Palindrome Number
Given an integer x, return true if x is a palindrome, and false otherwise.
Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 
Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        '''
        do we need to convert it to str? not really
        '''
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        #only need to reverse half of number x
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x = x // 10

        return x == reversed_half or x == reversed_half // 10 # eg  1221 vs. 12321
        #return str(x) == str(x)[::-1]
    def isPalindrome2(self, x: int) -> bool:
        '''
        convert to str
        '''
        s = str(x)
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    def isPalindrome3(self, x: int) -> bool:
        '''
        convert to str, pythonic
        '''
        s = str(x)
        return s == s[::-1]
if __name__ == "__main__":
    a = Solution()
    print(a.isPalindrome(121))
    print(a.isPalindrome(-121))
    print(a.isPalindrome(10))
    print(a.isPalindrome(12321))
    print(a.isPalindrome(123321))
    print(a.isPalindrome(0))