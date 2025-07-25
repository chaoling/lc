'''
1657. Determine if Two Strings Are Close
Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

Example 1:

Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"
Example 2:

Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.
Example 3:

Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"
 

Constraints:

1 <= word1.length, word2.length <= 105
word1 and word2 contain only lowercase English letters.
'''
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        from collections import Counter
        if set(word1) != set(word2): # abc vs def
            return False
        c1, c2 = list(Counter(word1).values()), list(Counter(word2).values())
        return sorted(c1) == sorted(c2)

if __name__ == "__main__":
    s = Solution()
    print(s.closeStrings("abc", "bca")) # true
    print(s.closeStrings("a", "aa")) # false
    print(s.closeStrings("cabbba", "abbccc")) # true
    print(s.closeStrings("cabbba", "aabbss")) # false
    print(s.closeStrings("uau", "ssx")) # false
    print(s.closeStrings("cabbba", "aabbcc")) # true
    print(s.closeStrings("cabbba", "aabbbcc")) # false