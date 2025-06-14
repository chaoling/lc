'''
Python bit manipulation is clean:

Operation	Code
Get bit	(n >> i) & 1
Set bit	`n
Clear bit	n &= ~(1 << i)
Toggle bit	n ^= (1 << i)
Count bits	bin(n).count('1')
Bit length	n.bit_length()
get lowest set bit	n & -n
is_power = n > 0 and (n & (n - 1)) == 0
Hamming weight is the number of 1's in the binary representation of a number.
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        for i in range(32):
            ans += (n >> i & 1)
        return ans
    def hammingWeight2(self, n: int) -> int:
        return bin(n).count('1')
    def hammingWeight3(self, n: int) -> int:
        return n.bit_length() - bin(n).rfind('1') - 1
    def hammingWeight4(self, n: int) -> int:
        ans = 0
        while n:
            ans += 1
            n &= (n - 1)
        return ans
    def hammingWeight5(self, n: int) -> int:
        return sum((n >> i) & 1 for i in range(32))
    def hammingWeight6(self, n: int) -> int:
        return sum(map(int, bin(n)[2:]))
    def hammingWeight7(self, n: int) -> int:
        return sum(int(c) for c in bin(n)[2:])
    def hammingWeight8(self, n: int) -> int:
        return bin(n).replace('0', '').count('1')

if __name__ == '__main__':
    n = 11
    print(Solution().hammingWeight(n))
    print(Solution().hammingWeight2(n))
    print(Solution().hammingWeight3(n))
    print(Solution().hammingWeight4(n))
    print(Solution().hammingWeight5(n))
    print(Solution().hammingWeight6(n))
    print(Solution().hammingWeight7(n))
    print(Solution().hammingWeight8(n))