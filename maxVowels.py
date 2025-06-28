'''
1456. Maximum Number of Vowels in a Substring of Given Length

Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length
'''
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        '''
        sliding windows of len k, subtract head and add tail, keep track of the max
        '''
        vowels = set('aeiou')
        current = sum(1 for c in s[:k] if c in vowels)
        max_count = current

        for i in range(k, len(s)):
            if s[i - k] in vowels:
                current -= 1
            if s[i] in vowels:
                current += 1
            max_count = max(max_count, current)

        return max_count
if __name__ == "__main__":
    s = "abciiidef"
    k = 3
    print(Solution().maxVowels(s, k))  # Output: 3
    s = "aeiou"
    k = 2
    print(Solution().maxVowels(s, k))  # Output: 2
    s = "leetcode"
    k = 3
    print(Solution().maxVowels(s, k))  # Output: 2
    s = "rhythms"
    k = 4
    print(Solution().maxVowels(s, k))  # Output: 0
    s = "tryhard"
    k = 4
    print(Solution().maxVowels(s, k))  # Output: 1