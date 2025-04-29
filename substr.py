'''
https://leetcode.com/problems/is-subsequence/
lc 392. Is Subsequence

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
 

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        '''
         Check if string s is a subsequence of string t.
         A subsequence maintains the order but may delete characters.
         i, j -> 0,0
         scan t[j] until find s[i], then advance i by 1
         j always forward one position regardless.
        '''
        if not s:
            return True #or False for empty str case

        n, m = len(s), len(t)
        i, j = 0, 0
        while i < n and j < m:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == n
    

import bisect
from collections import defaultdict

class SubsequenceChecker_jumptable:
    def __init__(self, t: str):
        # Preprocess t
        self.char_indices = defaultdict(list)
        for idx, ch in enumerate(t):
            self.char_indices[ch].append(idx)

    def isSubsequence(self, s: str) -> bool:
        curr_pos = -1  # Start before the beginning
        for ch in s:
            if ch not in self.char_indices:
                return False
            idx_list = self.char_indices[ch]
            # Find the smallest idx > curr_pos
            i = bisect.bisect_right(idx_list, curr_pos)
            if i == len(idx_list):
                return False
            curr_pos = idx_list[i]
        return True
        
class SubsequenceChecker:
    def __init__(self, t: str):
        n = len(t)
        self.next_pos = [dict() for _ in range(n + 1)]
        
        # Initialize the last row with "None"
        last = {chr(ord('a') + i): None for i in range(26)}
        self.next_pos[n] = last.copy()
        
        # Build from the end
        for i in range(n-1, -1, -1):
            last[t[i]] = i
            self.next_pos[i] = last.copy()

    def isSubsequence(self, s: str) -> bool:
        pos = 0
        for ch in s:
            if self.next_pos[pos].get(ch) is None:
                return False
            pos = self.next_pos[pos][ch] + 1
            if pos > len(self.next_pos) - 1:
                break
        return True

    
# Example usage:
checker = SubsequenceChecker("ahbgdc")
print(checker.isSubsequence("abc"))  # Output: True
# Example usage:
checker = SubsequenceChecker("ahbgdc")
print(checker.isSubsequence("axc"))  # Output: False
# Example usage:
checker = SubsequenceChecker("abcde")
print(checker.isSubsequence("ace"))  # Output: True