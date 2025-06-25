'''
1071. Greatest Common Divisor of Strings
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
 

Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.
'''
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Helper: compute GCD of two integers using the Euclidean algorithm
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # Compute GCD of the string lengths
        l1, l2 = len(str1), len(str2)
        n = gcd(l1, l2)
        candidate = str1[:n]  # Possible GCD string

        # Check if candidate repeated forms both strings
        if candidate * (l1 // n) == str1 and candidate * (l2 // n) == str2:
            return candidate
        else:
            return ""

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    print(sol.gcdOfStrings("ABCABC", "ABC"))  # Output: "ABC"
    print(sol.gcdOfStrings("ABABAB", "ABAB"))  # Output: "AB"
    print(sol.gcdOfStrings("LEET", "CODE"))    # Output: ""
    print(sol.gcdOfStrings("ABABAB", "ABABAB"))  # Output: "ABABAB"