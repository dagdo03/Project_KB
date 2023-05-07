# import list as List
import collections
from collections import deque

def ladderLength(beginWord: str, endWord: str, wordList) -> int:
    if endWord not in wordList:
        return 0
    
    nei = collections.defaultdict(list)
    wordList.append(beginWord)
    for word in wordList:
        for j in range(len(word)):
            pattern = word[:j] + "*" + word[j + 1:]
            nei[pattern].append(word)
            
    visit = set([beginWord])
    q = deque([beginWord])
    res = 1
    while q:
        for i in range(len(q)):
            word = q.popleft()
            if word == endWord:
                return res
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                for neiWord in nei[pattern]:
                    if neiWord in nei[pattern]:
                        visit.add(neiWord)
                        q.append(neiWord)
        res += 1
    return 0

beginWord = "hit"
endWord = "hot"
wordList = ["hot", "dot", "lot", "log", "cog"]
n = ladderLength(beginWord, endWord, wordList)
print(n)