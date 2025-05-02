from typing import List
'''
68. Text Justification

Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
 

Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.
Example 3:

Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
 

Constraints:

1 <= words.length <= 300
1 <= words[i].length <= 20
words[i] consists of only English letters and symbols.
1 <= maxWidth <= 100
words[i].length <= maxWidth
'''

from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        """
        Fully justify text using a greedy approach.
        Time: O(N), Space: O(N) for the output.
        """
        res: List[str] = []
        n = len(words)
        index = 0

        while index < n:
            # 1) Figure out how many words fit on this line
            sum_chars = len(words[index])
            last = index + 1
            while last < n and sum_chars + 1 + len(words[last]) <= maxWidth:
                sum_chars += 1 + len(words[last])
                last += 1

            line_words = words[index:last]
            num_words = last - index
            line = ""

            # 2) If this is the last line or only one word, left‐justify
            if last == n or num_words == 1:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
            else:
                # 3) Otherwise, fully justify
                # Total spaces we need = maxWidth − sum(len(word) for word in line_words)
                total_spaces = maxWidth - sum(len(w) for w in line_words)
                slots = num_words - 1
                space_width, extra = divmod(total_spaces, slots)

                for i in range(slots):
                    line += line_words[i]
                    # give one extra space to the first `extra` slots
                    line += " " * (space_width + (1 if i < extra else 0))
                line += line_words[-1]

            res.append(line)
            index = last

        return res

    
# Example usage
if __name__ == "__main__":
    sol = Solution()
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    result = sol.fullJustify(words, maxWidth)
    
    for line in result:
        print(f'"{line}"')
        # Output each justified line
    
    words2 = ["What","must","be","acknowledgment","shall","be"]
    maxWidth2 = 16
    result2 = sol.fullJustify(words2, maxWidth2)
    for line in result2:
        print(f'"{line}"')
        # Output each justified line
    
    words3 = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
    maxWidth3 = 20
    result3 = sol.fullJustify(words3, maxWidth3)
    for line in result3:
        print(f'"{line}"')
        # Output each justified line
    