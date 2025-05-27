'''
290. Word Pattern
https://leetcode.com/problems/word-pattern/
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.
 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"

Output: true

Explanation:

The bijection can be established as:

'a' maps to "dog".
'b' maps to "cat".
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"

Output: false

Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"

Output: false

 

Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        '''
        idea: use dictionary to map words to letters, and see if ther is a conflict or not
        '''
        hm, mh = {}, {}
        words = s.split()
        if len(pattern) != len(words):
            return False
        for i, word in enumerate(words):
            if word not in hm:
                hm[word] = pattern[i]
            if pattern[i] not in mh:
                mh[pattern[i]] = word

            if hm[word] != pattern[i] or mh[pattern[i]] != word:
                return False
        else:
            return True

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    print(sol.wordPattern("abba", "dog cat cat dog"))  # Output: True
    print(sol.wordPattern("abba", "dog cat cat fish"))  # Output: False
    print(sol.wordPattern("aaaa", "dog cat cat dog"))   # Output: False
    print(sol.wordPattern("abc", "a b c"))               # Output: True
    print(sol.wordPattern("abca", "a b c a"))           # Output: True