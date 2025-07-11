'''
338. Counting Bits

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
 

Constraints:

0 <= n <= 105
 
Follow up:

It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?
'''
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        '''
        how to do it in O(n) ?
        in binary form, from 0 -> n, everytime add 1 to the binary and compute the number of 1s
        '''
        ans = [0] * (n+1)
        for i in range(1,n+1):
            # 00000->00001->00010->00011->00100->00101->00110->00111->01000->01001->01010->01011->01100->01101->01110->01111...
            # observation: for even number from odd, just do left shift by 1
            '''
            if i % 2:
                ans.append(ans[-1]+1)
            else:
                a = 1 if i & (i-1) == 0 else ...
                ans.append(a)
            '''
            ans[i] = ans[i>>1] + (i & 1)
        return ans