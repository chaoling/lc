'''
28. Find the Index of the First Occurrence in a String
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        '''
        use two pointers, one at the begin of needle, one at the begin of haystack
        scan haystack for first letter match in needle, if match, scan the subsequent chr
        in needle if don't match, then restart the search from the 1st char of needle
        exit condition: either found the match, return the 1st occurance of haystack pointer or -1.
        Time complexity is roughly O(N * M) in worst-case scenarios, acceptable without using advanced algorithms like KMP.
        '''
        m, n = len(needle), len(haystack)
        if m == 0:
            return 0
        i = 0 #start index of haystack O(N)
        j = 0 #start index of needle O(M)
        while i < n:
            if haystack[i] != needle[j]:
                i += 1
            else:
                start = i
                while i < n and j < m and haystack[i] == needle[j]:
                    i += 1
                    j += 1
                if j == m:
                    # we found a full match of needle in haystack
                    # if j == m, it means we have matched all characters in needle
                    # and i is now at the next char after the last match
                    # so we can return the index of the first occurrence
                    # of needle in haystack, which is i - j
                    return start  # i is now at the next char after the last match, so we return i - j + 1
                else:
                    #no match, reset j to 0
                    i = start + 1  # move i back to the next char after the first match
                    j = 0

        return -1
    

    def strStrKMP(self, haystack: str, needle: str) -> int:
        def build_lps(pattern: str) -> list[int]:
            """
            Builds the Longest Prefix Suffix (LPS) array.
            lps[i] = length of the longest proper prefix which is also a suffix in pattern[0:i+1]
            """
            lps = [0] * len(pattern)
            length = 0  # Length of the previous longest prefix suffix
            i = 1

            while i < len(pattern):
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps

        if not needle:
            return 0  # Per problem definition

        lps = build_lps(needle)
        i = j = 0  # i = index for haystack, j = index for needle

        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == len(needle):
                    return i - j  # Match found
            else:
                if j > 0:
                    j = lps[j - 1]  # Use lps to avoid full reset
                else:
                    i += 1

        return -1  # No match found
# Time complexity: O(N * M) in the worst case, where N is the length of haystack and M is the length of needle
# Space complexity: O(1) since we are using only a few variables for indexing
# Example usage:
sol = Solution()
print(sol.strStr("hello", "ll"))  # Output: 2
print(sol.strStr("aaaaa", "bba"))  # Output: -1
print(sol.strStr("", ""))  # Output: 0
print(sol.strStr("haystack", ""))  # Output: 0
print(sol.strStr("a", "a"))  # Output: 0
print(sol.strStr("mississippi", "issip"))  # Output: 4

print(sol.strStrKMP("hello", "ll"))  # Output: 2
print(sol.strStrKMP("aaaaa", "bba"))  # Output: -1
print(sol.strStrKMP("", ""))  # Output: 0
print(sol.strStrKMP("haystack", ""))  # Output: 0
print(sol.strStrKMP("a", "a"))  # Output: 0
print(sol.strStrKMP("mississippi", "issip"))  # Output: 4