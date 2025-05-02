from typing import List


class Solution:
    def hindex(self, citations: List[int]) -> int:
        n = len(citations)
        if n == 0:
            return 0
        
        citations.sort(reverse=True)
        
        for i in range(n):
            if citations[i] < i + 1:
                return i
        
        return n

    def hindexbucket(self, citations: List[int]) -> int:
        '''
        Use a bucket sort approach to find the h-index.
        Time: O(N), Space: O(N)
        '''
        n = len(citations)
        if n == 0:
            return 0
        
        buckets = [0] * (n + 1)
        
        for c in citations:
            if c >= n:
                buckets[n] += 1
            else:
                buckets[c] += 1
        
        total = 0
        for i in range(n, -1, -1):
            '''
            Then you scan from high to low (since higher h-index is better):

            Accumulate total number of papers with ≥ i citations.

            When total >= i, that’s the maximum valid h-index.
            '''
            total += buckets[i]
            if total >= i:
                return i
        
        return 0
    
# Example usage:
sol = Solution()
print(sol.hindex([3, 0, 6, 1, 5]))  # Output: 3
print(sol.hindexbucket([3, 0, 6, 1, 5]))  # Output: 3       
print(sol.hindex([]))  # Output: 0
print(sol.hindexbucket([]))  # Output: 0
print(sol.hindex([1, 2, 3, 4, 5]))  # Output: 3
print(sol.hindexbucket([1, 2, 3, 4, 5]))  # Output: 3