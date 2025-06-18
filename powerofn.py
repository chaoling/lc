'''
50. Pow(x, n)
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
 

Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
n is an integer.
Either x is not zero or n > 0.
-104 <= xn <= 104
'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        '''
        1. floating point arithmetic, 
        2. do you do it in binary exponentiation or exponentiation by squaring
        3. treat positive exponent and negative one differently
        4. time complexity: O(log n), space complexity: O(1)
        5. edge case: n == 0, x == 0, x == 1, x == -1, n == -1
        6. iterative solution
        7. binary exponentiation: x^n = (x^(n//2)) * (x^(n//2)) if n is even, or x * (x^(n//2)) * (x^(n//2)) if n is odd
        8. exponentiation by squaring: x^n = (x^2)^(n//2)


        Start with ans = 1.0 (our result accumulator).
        Loop while n > 0:
        If the least significant bit (LSB) of n is 1 → multiply ans by x.
        Square x (because x^(2^i+1) = (x^(2^i))^2).
        Right-shift n by 1 (equivalent to n //= 2).
        '''
        if n == 0:
            return 1.0 # x**0 == 1
        if n < 0:
            x = 1/x
            n = -n
       
        ans = 1.0
        while n > 0:
            if n % 2 == 1: #if the least significant bit of n is 1
                ans *= x  # multiply ans by x
            x *= x # square x for the next iteration
            n //= 2 # right-shift n by 1 (equivalent to n //= 2)
        return ans