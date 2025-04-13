from collections import defaultdict, deque
from typing import List


def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''
        for each letter in the current word, build the adjacent list that only hase one letter 
        difference from the word list, this is a potentially valid path, so add it to the priority queue
        for futher processing. 
        end condition: the endWord is in the adjacent list, return the path len.
        hit-> hot->dot, lot, -> 
        '''
        '''
        for each letter in the current word, build the adjacent list that only hase one letter 
        difference from the word list, this is a potentially valid path, so add it to the priority queue
        for futher processing. 
        end condition: the endWord is in the adjacent list, return the path len.
        hit-> hot->dot, lot, -> 
        '''
        from collections import deque
        def letterDistance(w1: str, w2: str) -> int:
            '''
            given two words of same len, return the number of chars that differs
            O(len(w))
            '''
            cnt = 0
            for i,a in enumerate(w1):
                if a != w2[i]:
                    cnt += 1
            return cnt

        if endWord not in wordList:
            return 0
        qu = deque()
        visited = set()
        qu.append((beginWord,1))
        visited.add(beginWord)
        while qu:
            cur_word, path_len = qu.popleft()
            #find all word in the wordList that has letterDistance of 1 to the current word
            for w in wordList:
                if w not in visited and letterDistance(cur_word, w) == 1:
                    if w == endWord:
                        return path_len + 1
                    qu.append((w,path_len+1))
                    visited.add(w)
        else:
            return 0 # no solution  
        
def ladderLength_optimized(beginWord: str, endWord: str, wordList: list[str]) -> int:
    '''
    strategy: instead of checking all wordList everytime, create a dict of list that
    uses on letter position in begi this step changes O(n*m) to O(m*26)
    '''
    # step one: initialize variables and build up dicts
    visited = set()
    L = len(beginWord)
    # Preprocessing: Create a pattern map like h*t -> [hot, hit]
    pattern_map = defaultdict(list)
    for word in wordList:
        for i in range(L):
            pattern = word[:i] + '*' + word[i+1:]
            pattern_map[pattern].append(word)
    
    qu = deque([(beginWord, 1)])
    while qu:
        cur_word, path_len = qu.popleft()
        for i in range(L):
            pattern = cur_word[:i] + "*" + cur_word[i+1:]
            for neighbor in pattern_map[pattern]:
                if neighbor == endWord:
                    return path_len + 1
                if neighbor not in visited:
                    visited.add(neighbor)
                    qu.append((neighbor, path_len + 1))
    return 0

if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    print(ladderLength_optimized(beginWord, endWord, wordList))