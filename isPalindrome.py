'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.'''
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        many ways to do it, recursive, iterative, etc.
        '''
        # convert all to lower case
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        n = len(s)
        for i in range(n//2):
            if s[i] != s[-1-i]:
                return False
        
        return True
        def helper(s: str) -> bool:
            if not s or len(s) == 1:
                return True
            else:
                return s[0] == s[-1] and helper(s[1:-1])
        # return helper(s)
# test cases
s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama")) # True
