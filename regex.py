'''
10. Regular Expression Matching
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        dp[i][j] is True iff s[i:] matches p[j:]
        Answer is dp[0][0]
        '''
        m, n = len(s), len(p)
        # Allocate dp[m+1][n+1]
        dp = [[False] * (n+1) for _ in range(m+1)]
        dp[m][n] = True
        for i in range(m, -1, -1):
            for j in range(n-1, -1, -1):
                # Can we match one char?
                first_match = (i < m) and (s[i] == p[j] or p[j] == '.')
                # Handle '*' as p[j+1]
                if j+1 < n and p[j+1] == '*':
                    # Zero occurrences of p[j] or at least one (stay on j)
                    dp[i][j] = dp[i][j+2] or (first_match and dp[i+1][j])
                else:
                    # Must consume one char in both s and p
                    dp[i][j] = first_match and dp[i+1][j+1]
        return dp[0][0]

# Test
if __name__ == "__main__":
    s = Solution()
    print(s.isMatch("aa", "a"))  # Output: False
    print(s.isMatch("aa", "a*"))  # Output: True
    print(s.isMatch("ab", ".*"))  # Output: True
    print(s.isMatch("aab", "c*a*b"))  # Output: True
    print(s.isMatch("mississippi", "mis*is*p*."))  # Output: False
    print(s.isMatch("ab", ".*c"))  # Output: False