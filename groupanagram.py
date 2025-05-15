'''
49. Group Anagrams
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
'''
from typing import List, Dict
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        what is anagrams? what do they have in common?
        can we use a hash function? hash(word) => sum of all chars in words? not collision proof!
        use a set to store all hashed values
        use sorted string as the key!!!

        '''
        anagram_map = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            #key = tuple([word.count(c) for c in 'abcdefghijklmnopqrstuvwxyz'])
            anagram_map[key].append(word)

        return list(anagram_map.values())

if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    print(s.groupAnagrams([""]))
    print(s.groupAnagrams(["a"]))
    print(s.groupAnagrams(["a","b","c"]))
    print(s.groupAnagrams(["a","b","c","a"]))
    print(s.groupAnagrams(["a","b","c","a","b"]))
    print(s.groupAnagrams(["a","b","c","a","b","c"]))
    print(s.groupAnagrams(["a","b","c","a","b","c","a"]))
    print(s.groupAnagrams(["a","b","c","a","b","c","a","b"]))
    print(s.groupAnagrams(["a","b","c","a","b","c","a","b","c"]))
    print(s.groupAnagrams(["a","b","c","a","b","c","a","b","c","a"]))
    print(s.groupAnagrams(["a","b","c","a","b","c","a","b","c","a","b"]))
    print(s.groupAnagrams(["a","b","c","a","b","c","a","b","c","a","b","c"]))