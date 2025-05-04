from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        1) check the 1st letter of all words, if eaqual, repeat for the next letter, until one of the position differ
        '''
        n = len(strs)
        index = 0
        res = []
        early_break = False
        while not early_break:
            for i in range(n):
                if index >= len(strs[i]) or strs[i][index] != strs[0][index]:
                    early_break = True
                    break
            else:
                res.append(strs[0][index])

            index += 1
        return ''.join(res)

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
    print(sol.longestCommonPrefix(["dog", "racecar", "car"]))  # Output: ""
    print(sol.longestCommonPrefix([""]))  # Output: ""
    print(sol.longestCommonPrefix(["a"]))  # Output: "a"
