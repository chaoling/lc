'''
212. Word Search II

Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example 1:


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:


Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
'''
class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children: dict[str, TrieNode] = {} #dictionary of key: current str value: trienodes

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word:str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_end = True
    
    def search(self, word: str) -> bool:
        # helper function for dfs
        def _search_from(node: TrieNode, suffix: str) -> bool:
            if not suffix:
                return node.is_end
            ch, rest = suffix[0], suffix[1:]
            if ch in node.children:
                return _search_from(node.children[ch], rest)
            return False

        return _search_from(self.root, word)

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        '''
        graph problem? can walk left->right and right->left? up->bottom and bottom->up?
        how to quickly tell if a path is valid (aka a word or not?) using trie?
        build a trie using words?
        '''
        m, n = len(board), len(board[0])
        res = set() #avoid duplicate
        # use words to build up the Trie so we can do quick search
        trie = Trie()
        for word in words:
            trie.insert(word)

        def dfs(i: int, j: int, node: TrieNode, path: str) -> None:
            '''
            from coord i,j do dfs and return if a valid word is found and add it to result set
            '''
            ch = board[i][j]
            if ch not in node.children:
                return
            node = node.children[ch]
            path += ch
            if node.is_end:
                res.add(path)
            board[i][j] = "#" #mark as visited

            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]: # up, down, left, right
                ni, nj = i+dx, j+dy
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] != "#":
                    dfs(ni, nj, node, path)
            
            #back track:
            board[i][j] = ch #backtrack
        
        for i in range(m):
            for j in range(n):
                dfs(i, j, trie.root, "")
        
        return list(res)