'''
839. Similar String Groups
Companies
Two strings, X and Y, are considered similar if either they are identical or we can make them equivalent by swapping at most two letters (in distinct positions) within the string X.

For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".

Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.

We are given a list strs of strings where every string in strs is an anagram of every other string in strs. How many groups are there?

 

Example 1:

Input: strs = ["tars","rats","arts","star"]
Output: 2
Example 2:

Input: strs = ["omv","ovm"]
Output: 1
 

Constraints:

1 <= strs.length <= 300
1 <= strs[i].length <= 300
strs[i] consists of lowercase letters only.
All words in strs have the same length and are anagrams of each other.
'''
from typing import List

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        '''
        1) def a function called similar : they are all anagrams of each other, so just count number of positions that the chars are different, if it is less or equal to 2, they are similar, otherwise not similar.
        2) use union-find algorithm to union all similar strs together in one connected components
        the number of groups are between 1 (all similar to each other) and n (none of them are similar)
        '''
        #strs contains list of isolated groups of size 1
        n = len(strs)
        parent = list(range(n))
        rank = [0] * n
        #we do not care about size in the group, just need to know how many groups

        def is_similar(s1, s2) -> bool:
            # assumption: s1 and s2 are anagrams of each other
            assert len(s1) == len(s2)
            diff = 0
            for ca, cb in zip(s1, s2):
                if ca != cb:
                    diff += 1
                    if diff > 2:
                        return False
            return diff == 2 or diff == 0
        
        def union(x: int, y: int) -> bool:
            px, py = find(x), find(y)
            if px == py:
                #they already are one group
                return False
            #if rank[px] < rank[py]:
                #px, py = py, px
            parent[py] = px
            #if rank[px] == rank[py]:
                #rank[px] += 1
            return True

        def find(x) -> int:
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        groups = n
        for i in range(n):
            for j in range(i+1, n):
                if is_similar(strs[i],strs[j]):
                    if union(i, j):
                        groups -= 1

        return groups