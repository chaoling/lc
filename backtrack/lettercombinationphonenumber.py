'''
17. Letter Combinations of a Phone Number
Medium
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
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        '''
        create a map between num->{letters},
        for each level of digits, try each letter in the map backtracking
        '''
        ans = []
        n = len(digits)
        phone_number = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'], '5': ['j','k','l'],
                         '6': ['m','n','o'], '7': ['p','q','r','s'], '8':['t','u','v'], '9': ['w','x','y','z']}
        def backtracking(path: List[str], index: int):
            if n == index:
                ans.append(''.join(path))
            else:
                for letter in phone_number[digits[index]]:
                        path.append(letter)
                        backtracking(path, index+1)
                        path.pop()
        
        if not digits:
            return []
        backtracking([],0)
        return ans
if __name__ == '__main__':
    test = [
        "23",
        "",
        "2",
        "79"
    ]
    for digits in test:
        print(f'digits={digits} => {Solution().letterCombinations(digits)}')    