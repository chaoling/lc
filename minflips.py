'''
1318. Minimum Flips to Make a OR b Equal to c
Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.
Example 1:

Input: a = 2, b = 6, c = 5
Output: 3
Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)
Example 2:

Input: a = 4, b = 2, c = 7
Output: 1
Example 3:

Input: a = 1, b = 2, c = 3
Output: 0
 
Constraints:

1 <= a <= 10^9
1 <= b <= 10^9
1 <= c <= 10^9
'''
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        '''
        check the bits one by one, how?
        0bit: a & 1
        1bit: a >> 1 & 1
        ibit: a >> i & 1
        '''
        flip = 0
        while (a != 0 or b != 0 or c != 0):
            ap, bp, cp = a & 1, b & 1, c & 1
            if ap | bp != cp:
                if cp == 1 or (cp == 0 and ap != bp):
                    flip += 1 #ap , bp = 0, 0 or 0, 1 or 1, 0
                elif cp == 0 and ap == 1 and bp == 1:
                    flip += 2
            a >>= 1
            b >>= 1
            c >>= 1
        return flip
if __name__ == '__main__':
    test = [
        [2, 6, 5],
        [4, 2, 7],
        [1, 2, 3],
        [1, 0, 0],
        [0, 0, 0],
        [1, 1, 1],
        [2, 3, 4]
    ]
    for a,b,c in test:
        print(f'a={a}, b={b}, c={c} => {Solution().minFlips(a,b,c)}')