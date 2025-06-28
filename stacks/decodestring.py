'''
394. Decode String
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
 

Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
'''
class Solution:
    def decodeString(self, s: str) -> str:
        ''' 
        use a stack, push char one by one until you met a right bracket, the process until you see left bracket, then repeat n   times
        '''
        stk = []
        digits = set('0123456789')
        for c in s:
            if c != ']':
                stk.append(c)
            else:
                subs = ""
                #extract substrs
                substr = [] 
                while stk:
                    tmp = stk.pop()
                    if tmp == '[':
                        break
                    substr.append(tmp)
                substr = substr[::-1]
                subs = ''.join(substr)
                multi = []
                nums = 1
                # extract multipliers
                while stk and stk[-1] in digits:
                    multi.append(stk.pop())
                    nums = multi[::-1]
                    nums =int(''.join(nums))

                expansion_str = subs * nums
                for c in expansion_str:
                    stk.append(c)
        return ''.join(stk)

if __name__ == "__main__":  
    s = Solution()
    print(s.decodeString("3[a]2[bc]"))  # Output: "aaabcbc"
    print(s.decodeString("3[a2[c]]"))  # Output: "accaccacc"
    print(s.decodeString("2[abc]3[cd]ef"))  # Output: "abcabccdcdcdef"
    print(s.decodeString("abc3[cd]xyz"))  # Output: "abccdcdcdxyz"
    print(s.decodeString("10[a]"))  # Output: "aaaaaaaaaa"
    print(s.decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"))  # Output: "zzzyypqjkjkefjkjkefjkjkefjkjkefef"
    print(s.decodeString("2[3[a]b]"))  # Output: "aaabaaab"