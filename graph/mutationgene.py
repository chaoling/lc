'''
433. Minimum Genetic Mutation

A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.

Example 1:

Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1
Example 2:

Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2
 

Constraints:

0 <= bank.length <= 10
startGene.length == endGene.length == bank[i].length == 8
startGene, endGene, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].
'''
from collections import deque
from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        '''
        use BFS, would it make sense to convert bank from list to set? o(1) look up
        but if the bank is only 10 items max, it should not matter much 
        how to determine next valid mutation ? 
        how to track visited gene mutations?
        '''
        bank = set(bank)
        q = deque([(startGene, 0)])
        nucleotides = ['A', 'C', 'G', 'T']
        visited = set(startGene)

        while q:
            nxtGene, step = q.popleft()
            if nxtGene == endGene:
                return step
            else:
                #change one genome at a time
                for i in range(len(nxtGene)):
                    cur_char = nxtGene[i]
                    for new_char in [ch for ch in nucleotides if ch != cur_char]:
                        new_gene = nxtGene[:i] + new_char + nxtGene[i+1:]
                        if new_gene not in visited and new_gene in bank:
                            visited.add(new_gene)
                            q.append((new_gene, step+1))
        return -1