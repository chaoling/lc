'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
'''
from typing import List

def letterCombinations(digits: str) -> List[str]:
    '''
    usig dfs with backtrackning
    '''
    # build the graph using list of list
    graph =[['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
    #2->9 map to index 0->7
    output, path = [], []
    if not digits:
        return []
    n = len(digits)
    def dfs(graph: List[List], level, path):
        index = int(digits[level]) - 2
        for ch in graph[index]:
            #print(f"now exam... {ch=}")
            path.append(ch)
            if level < n-1:
                dfs(graph, level+1, path)
            else:
                output.append(''.join(path))
            path.pop()
    
    dfs(graph, 0, path)
    return output

if __name__ == "__main__":
    print(letterCombinations("23"))