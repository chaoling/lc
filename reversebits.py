'''
190. Reverse Bits

Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type. They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above, the input represents the signed integer -3 and the output represents the signed integer -1073741825.
 
Example 1:

Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
Example 2:

Input: n = 11111111111111111111111111111101
Output:   3221225471 (10111111111111111111111111111111)
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.
 

Constraints:

The input must be a binary string of length 32
 

Follow up: If this function is called many times, how would you optimize it?
'''
class Solution:
    def reverseBits(self, n: int) -> int:
        ans = []
        for i in range(32):
            bit = n >> i & 1
            ans.append(str(bit))
        res = ''.join(ans)
        return int(res,2)
    
    
    def reverseBits2(self, n: int) -> int:
        ans = 0
        for i in range(32):
            bit = n >> i & 1
            ans = ans | (bit << (31 - i))
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.reverseBits(43261596)) # 964176192
    print(s.reverseBits(4294967293)) # 3221225471
    print(s.reverseBits(0)) # 0
    print(s.reverseBits(1)) # 2147483648
    print(s.reverseBits(2)) # 1073741824
    print(s.reverseBits(3)) # 3221225472
    print(s.reverseBits(4)) # 536870912
    print(s.reverseBits(5)) # 2684354560
    print(s.reverseBits(6)) # 1610612736
    print(s.reverseBits(7)) # 3758096384
    print(s.reverseBits(8)) # 134217728
    print(s.reverseBits(9)) # 4026531840
    print(s.reverseBits(10)) # 2013265920
    print(s.reverseBits(11)) # 3489660928
    print(s.reverseBits(12)) # 671088640