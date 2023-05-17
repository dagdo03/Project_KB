# import list as List
import collections
from collections import deque

# def ladderLength(beginWord: str, endWord: str, wordList) -> int:
#     if endWord not in wordList:
#         return 0
    
#     nei = collections.defaultdict(list)
#     wordList.append(beginWord)
#     for word in wordList:
#         for j in range(len(word)):
#             pattern = word[:j] + "*" + word[j + 1:]
#             nei[pattern].append(word)
            
#     visit = set([beginWord])
#     q = deque([beginWord], [])
#     res = 1
#     while q:
#         for i in range(len(q)):
#             word = q.popleft()
#             # print(word + "->", end =" ")
#             if word == endWord:
#                 return res
#             for j in range(len(word)):
#                 pattern = word[:j] + "*" + word[j + 1:]
#                 for neiWord in nei[pattern]:
#                     if neiWord in nei[pattern]:
#                         visit.add(neiWord)
#                         q.append(neiWord)
#         # print(word + "->", end =" ")
#         res += 1
#     return 0

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
            
    visit = {beginWord: None}  # store the parent node of beginWord as None
    q = deque([beginWord])
    while q:
        word = q.popleft()
        if word == endWord:
            # construct the path by backtracking from endWord to beginWord
            path = [endWord]
            while word != beginWord:
                path.append(visit[word])
                word = visit[word]
            return path[::-1]  # reverse the path to get it from beginWord to endWord
        for j in range(len(word)):
            pattern = word[:j] + "*" + word[j + 1:]
            for neiWord in nei[pattern]:
                if neiWord not in visit:
                    visit[neiWord] = word  # store the parent node of neiWord
                    q.append(neiWord)
    return []

# def ladderLength(beginWord, endWord, wordList):
#     if endWord not in wordList:
#         return 0
    
#     nei = collections.defaultdict(list)
#     wordList.append(beginWord)
#     for word in wordList:
#         for j in range(len(word)):
#             pattern = word[:j] + "*" + word[j + 1:]
#             nei[pattern].append(word)
            
#     path_list = [[beginWord]]
#     path_index = 0
#     # To keep track of previously visited nodes
#     previous_nodes = {beginWord}
#     if beginWord == endWord:
#         return path_list[0]
        
#     while path_index < len(path_list):
#         current_path = path_list[path_index]
#         last_node = current_path[-1]
#         next_nodes = nei[last_node]
#         # Search goal node
#         if endWord in next_nodes:
#             current_path.append(endWord)
#             return current_path
#         # Add new paths
#         for next_node in next_nodes:
#             if not next_node in previous_nodes:
#                 new_path = current_path[:]
#                 new_path.append(next_node)
#                 path_list.append(new_path)
#                 # To avoid backtracking
#                 previous_nodes.add(next_node)
#         # Continue to next path in list
#         path_index += 1
#     # No path is found
#     return []

beginWord = "hit"
endWord = "lot"
wordList = ["hot", "dot", "lot", "log", "cog"]
n = ladderLength(beginWord, endWord, wordList)
print(n)