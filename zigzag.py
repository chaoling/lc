class Solution:
    '''
    6. Zigzag Conversion
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
'''
    def convert(self, s: str, numRows: int) -> str:
        '''
        what is the pattern for zigzag conversion?
        for each row:
        start with row id, then skip row_id%numRows , numRows*2-2-row_id
        numRows: 4
        row_id: 0.   1.    2.      3
        skip:   6.  4+2   2+4.   6

        '''
        n = len(s)
        res = [''] * numRows
        if numRows == 1 or numRows >= n:
            return s
        going_down = False
        curr_row = 0
        for c in s:
            res[curr_row] += c
            if curr_row == 0 or curr_row == numRows - 1:
                going_down = not going_down
            curr_row += 1 if going_down else -1
        return ''.join(res)
    
# Test
if __name__ == "__main__":
    s = Solution()
    print(s.convert("PAYPALISHIRING", 3))  # Output: "PAHNAPLSIIGYIR"
    print(s.convert("PAYPALISHIRING", 4))  # Output: "PINALSIGYAHRPI"
    print(s.convert("A", 1))  # Output: "A"
    print(s.convert("AB", 1))  # Output: "AB"
    print(s.convert("AB", 2))  # Output: "AB"
    print(s.convert("AB", 3))  # Output: "AB"