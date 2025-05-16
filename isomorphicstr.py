'''
205. Isomorphic Strings
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"

Output: true

Explanation:

The strings s and t can be made identical by:

Mapping 'e' to 'a'.
Mapping 'g' to 'd'.
Example 2:

Input: s = "foo", t = "bar"

Output: false

Explanation:

The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

Example 3:

Input: s = "paper", t = "title"

Output: true

 

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        '''
        key idea is like a cypher, one letter is mapped to another letter, one to one 
        mapping only.
        algorithm: scan the string in s and t one char at a time, (foo, bar)
        create a hashmap along the way, say : f-> b, o->a, if seen, say 2nd o is there, check if h(o)-> a is equal to 'r', if not, return false.
        O(N)
        '''
        n, m = len(s), len(t)
        if n != m:
            return False
        t2s, s2t = {}, {}
        for a, b  in zip(s,t):
            if a in s2t and s2t[a] != b or b in t2s and t2s[b] != a:
                return False
            s2t[a] = b
            t2s[b] = a
        return True
# test cases
s = Solution()
print(s.isIsomorphic("egg", "add")) # True
print(s.isIsomorphic("foo", "bar")) # False
print(s.isIsomorphic("paper", "title")) # True  
print(s.isIsomorphic("bade", "babe")) # False