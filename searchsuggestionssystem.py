'''
1268. Search Suggestions System
Medium
https://leetcode.com/problems/search-suggestions-system/
You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return a list of lists of the suggested products after each character of searchWord is typed.

 

Example 1:

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"].
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"].
After typing mou, mous and mouse the system suggests ["mouse","mousepad"].
Example 2:

Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
Explanation: The only word "havana" will be always suggested while typing the search word.
 

Constraints:

1 <= products.length <= 1000
1 <= products[i].length <= 3000
1 <= sum(products[i].length) <= 2 * 104
All the strings of products are unique.
products[i] consists of lowercase English letters.
1 <= searchWord.length <= 1000
searchWord consists of lowercase English letters.
'''
from typing import List


class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children: dict[str, TrieNode] = {}

class Trie:
    def __init__(self):
        self.root = TrieNode() #root is empty on purpose
        self.words = [] #list of words that matches the search suffix
    
    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_end = True

    def dfs(self, node: TrieNode, path: str, res: List[str]):
        if len(res) >= 3:
            return
        if node.is_end:
            res.append(path)
        for ch in sorted(node.children.keys()):
            self.dfs(node.children[ch], path + ch, res)

    def get_suggestions(self, prefix: str) -> List[str]:
        node = self.root
        # first travel to the common prefix node:
        for ch in prefix:
            if ch not in node.children:
                return [] #end early as the prefix not in trie
            node = node.children[ch]

        res = []
        self.dfs(node, prefix, res)
        return res[:3]
        


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        '''
        use prefix tree or tries to do the search
        '''
        trie = Trie()
        for word in products:
            trie.insert(word)
        
        results = []
        prefix = ""
        for ch in searchWord:
            prefix += ch
            results.append(trie.get_suggestions(prefix))
        return results
if __name__ == '__main__':
    test = [
        [["mobile","mouse","moneypot","monitor","mousepad"], "mouse"],
        [["havana"], "havana"],
        [["bags","baggage","banner","box","cloths"], "bags"]
    ]
    for products, searchWord in test:
        print(f'products={products}, searchWord={searchWord} => {Solution().suggestedProducts(products, searchWord)}')