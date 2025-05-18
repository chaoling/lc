# -*- coding: utf-8 -*-
'''
30. Substring with Concatenation of All Words
You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

 

Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]

Output: [0,9]

Explanation:

The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

Output: []

Explanation:

There is no concatenated substring.

Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

Output: [6,9,12]

Explanation:

The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].

 

Constraints:

1 <= s.length <= 104
1 <= words.length <= 5000
1 <= words[i].length <= 30
s and words[i] consist of lowercase English letters.
'''
from typing import List


class Solution:
    def findSubstringNaiveSolution(self, s: str, words: List[str]) -> List[int]:
        '''
        1) compute all permutation of substring concatinated str? powerset 2^N?
        2) use KMP to search matched patterns? o(N) ?
        '''
        def dfs(wordlist, path, seen, result):
            if len(path) == len(wordlist):
                result.append("".join(path))
                return 
            for i in range(len(wordlist)):
                if not seen[i]:
                    seen[i] = True
                    path.append(wordlist[i])
                    dfs(wordlist, path, seen, result)
                    path.pop()
                    seen[i] = False

        result, path = [], []
        n = len(words)
        seen = [False] * n
        dfs(words, path, seen, result)

        # Step 2: Search for the concatenated strings in s
        indices = []
        word_length = len(words[0])
        total_length = n * word_length
        for i in range(len(s) - total_length + 1):
            substring = s[i:i + total_length]
            if substring in result:
                indices.append(i)
        return indices
    
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        '''We're using a moving window of fixed size.
            A Counter keeps track of required words and their counts.
            We dynamically slide and adjust the window based on what's inside.
            It works in O(N) time where N is the length of s, avoiding O(N!) permutations.
        '''
        total_words = len(words)
        word_length = len(words[0])
        total_length = total_words * word_length
        word_count = {}
        for word in words:  # Count the occurrences of each word in the list
            word_count[word] = word_count.get(word, 0) + 1
        indices = []
        for i in range(len(s) - total_length + 1):
            seen = {}
            for j in range(total_words):
                word = s[i + j * word_length:i + (j + 1) * word_length]
                if word not in word_count:
                    break
                seen[word] = seen.get(word, 0) + 1
                if seen[word] > word_count[word]:
                    break
            else:
                indices.append(i)
        return indices
    
    def findSubstringOptimized(self, s: str, words: List[str]) -> List[int]:
        '''Optimized version of the above function using a sliding window approach.
           It uses a single loop to check for valid substrings without nested loops.
        '''
        if not s or not words:
            return []
        
        word_length = len(words[0])
        total_length = len(words) * word_length
        word_count = {}
        
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        
        indices = []
        for i in range(word_length):
            left = i
            right = i
            seen = {}
            while right + word_length <= len(s):
                word = s[right:right + word_length]
                right += word_length
                
                if word in word_count:
                    seen[word] = seen.get(word, 0) + 1
                    # Check if the word count exceeds the expected count, move left pointer if necessary 
                    while seen[word] > word_count[word]:
                        left_word = s[left:left + word_length]
                        seen[left_word] -= 1
                        left += word_length
                    
                    if right - left == total_length:
                        indices.append(left)
                else:
                    seen.clear()
                    left = right
        return indices
        
        
if __name__ == '__main__':
    s = "barfoothefoobarman"
    words = ["foo","bar"]
    print(Solution().findSubstring(s, words))
    s = "wordgoodgoodgoodbestword"
    words = ["word","good","best","word"]
    print(Solution().findSubstring(s, words))
    s = "barfoofoobarthefoobarman"
    words = ["bar","foo","the"]
    print(Solution().findSubstring(s, words))
    s = "wordgoodgoodgoodbestword"
    words = ["word","good","best","word"]
    print(Solution().findSubstring(s, words))
        