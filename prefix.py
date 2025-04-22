class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children: dict[str, TrieNode] = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_end = True

    def search(self, word: str) -> bool:
        # inner helper closes over `self`
        def _search_from(node: TrieNode, suffix: str) -> bool:
            if not suffix:
                return node.is_end

            ch, rest = suffix[0], suffix[1:]
            if ch == '.':
                # try every possible path
                return any(_search_from(child, rest)
                           for child in node.children.values())
            if ch in node.children:
                return _search_from(node.children[ch], rest)
            return False

        return _search_from(self.root, word)

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return True

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
