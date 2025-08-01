'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
'''
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import defaultdict
        fq= defaultdict( int )
        for w in magazine:
            fq[w] += 1
        
        for letter in ransomNote:
            if letter not in fq:
                return False
            else:
                if fq[letter] == 0:
                    return False
                else:
                    fq[letter] -= 1
        else:
            return True