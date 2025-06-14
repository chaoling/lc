'''
67. Add Binary

Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # convert a,b to list
        la, lb = [int(ch) for ch in a], [int(ch) for ch in b]
        n, m = len(la), len(lb)
        if n < m:
            la, lb = lb, la # la is longer or equal len with lb
            n, m = m, n
        i, carry = 0,0
        while i <= n-1:
            if i <= m-1:
                la[n-i-1] = la[n-i-1] + lb[m-i-1] + carry
            else:
                la[n-i-1] = la[n-i-1] + carry
            if la[n-i-1] > 1:
                carry = la[n-i-1] // 2
                la[n-i-1] = la[n-i-1] % 2
            else:
                carry = 0
            i += 1
        ans = ''.join(map(str,la))
        ans = '1' + ans if carry else ans
        return ans
    
    def AddBinary2(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        res = []
        
        while i >= 0 or j >= 0 or carry:
            total = carry
            
            if i >= 0:
                total += int(a[i])
                i -= 1
            
            if j >= 0:
                total += int(b[j])
                j -= 1
            
            carry = total // 2
            res.append(str(total % 2))
        
        return ''.join(reversed(res))
    
    def addBinary3(self, a: str, b: str) -> str:
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        
        carry = 0
        result = []
        
        for i in range(max_len - 1, -1, -1):
            bit_a = int(a[i])
            bit_b = int(b[i])
            
            total = bit_a + bit_b + carry
            carry = total // 2
            result.append(str(total % 2))
        
        if carry:
            result.append('1')
        
        return ''.join(reversed(result))
    def addBinary4(self, a: str, b: str) -> str:
        # convert a,b to list
        la, lb = [int(ch) for ch in a], [int(ch) for ch in b]
        n, m = len(la), len(lb)
        if n < m:
            la, lb = lb, la # la is longer or equal len with lb
            n, m = m, n
        i, carry = 0,0
        for i in range(1, n + 1):
            idx_a = n - i
            idx_b = m - i
            la[idx_a] += (lb[idx_b] if idx_b >= 0 else 0) + carry
            carry = la[idx_a] // 2
            la[idx_a] %= 2
        ans = ''.join(map(str,la))
        ans = '1' + ans if carry else ans
        return ans
if __name__ == "__main__":
    s = Solution()
    print(s.addBinary("11","1")) # 100
    print(s.addBinary("1010","1011")) # 10101
    print(s.addBinary("0","0")) # 0
    print(s.addBinary("1111","1111")) # 11110
    print(s.addBinary("1010000010010011011001000001010111101101100110111011111111110100000111111000110000000000000000",
                      "1101010010111011100011111001100010101000011010111010100000110110110010111011110011000000110111100110")) # 1101110101001111111011111101111011111111111001111111111111111110
    print(s.addBinary("101111","10")) # 110001