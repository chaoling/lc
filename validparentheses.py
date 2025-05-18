'''
20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''
class Solution:
    def isValid(self, s: str) -> bool:
        '''
        ds: use a stack
        algo: push open brackets onto stack, when encounter a close brackets, pop the stack and find a match,
        continue, if not match, return False early
        '''
        stk = []
        hf = {"(":")","[":"]","{":"}"}
        for st in s:
            if st in ('([{'):
                stk.append(st)
            if st in (')]}'):
                if not stk or hf[stk.pop()] != st:
                    return False
        return not stk
# test
if __name__ == "__main__":
    s = Solution()
    print(s.isValid("()")) # True
    print(s.isValid("()[]{}")) # True
    print(s.isValid("(]")) # False
    print(s.isValid("([])")) # True
    print(s.isValid("{[()]}")) # True
    print(s.isValid("{[(])}")) # False
    print(s.isValid("{[}")) # False