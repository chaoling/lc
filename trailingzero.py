'''
172. Factorial Trailing Zeroes
Given an integer n, return the number of trailing zeroes in n!.
Example 1:
Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:
Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Example 3:
Input: n = 0
Output: 0
Explanation: 0! = 1, no trailing zero.
Example 4:
Input: n = 10
Output: 2
Explanation: 10! = 3628800, two trailing zeroes.
Example 5:
Input: n = 25
Output: 6
Explanation: 25! = 15511210043330985984000000, six trailing zeroes.
Example 6:
Input: n = 100
Output: 24
Explanation: 100! = 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000, 24 trailing zeroes.
Constraints:
0 <= n <= 10^4
'''
class Solution:
    def trailingZeroes(self, n: int) -> int:
        def fact(n):
            prod = 1
            for i in range(1,n+1):
                prod *= i
            return prod
        
        if n == 0: 
            return 0
        else:
            num = fact(n)
            t = 0
            while num > 0:
                if num % 10 == 0:
                    t += 1
                else:
                    return t
                num = num // 10
            return t
    def trailingZeroes2(self, n: int) -> int:
        '''
        The problem can be solved without computing n!, 
        since trailing zeros come from pairs of factors of 2 and 5. 
        Since there are always more 2s than 5s, 
        we can just count how many times 5 appears as a factor.
        count how many 5s in the factorization of n!
        '''
        # Count the number of 5s, 25s, 125s, etc. in the factors
        count = 0
        while n > 0:
            n //= 5
            count += n
        return count
if __name__ == "__main__":
    a = Solution()
    print(a.trailingZeroes(3))
    print(a.trailingZeroes(5))
    print(a.trailingZeroes(0))
    print(a.trailingZeroes(10))
    print(a.trailingZeroes(25))
    print(a.trailingZeroes(100))