from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Trying transposition

        O(n * L), time to build adjacency list
        O(n), space to store adjacency list
        """
        words = set(wordList)
        if endWord not in words:
            return 0
        
        if beginWord not in words:
            words.add(beginWord)

        adj_list = defaultdict(list)

        for word in words:

            for i in range(len(word)):
                
                # replace character at index i with letters
                # form 'a' at 'z' and see if result is in words
                # if so an edge exists
                for j in range(ord('a'), ord('z') + 1):
                    replacement = chr(j)

                    if replacement == word[i]:
                        continue

                    transposition = "".join([
                        word[:i], replacement, word[i + 1:]
                    ])

                    if transposition in words:
                        adj_list[word].append(transposition)
                        adj_list[transposition].append(word)

        # bfs to find shortest path
        q = deque([beginWord])
        visited = set([beginWord])
        steps = 0

        while q:
            steps += 1

            for _ in range(len(q)):
                cur = q.popleft()

                for neighbor in adj_list[cur]:
                    if neighbor in visited:
                        continue

                    q.append(neighbor)
                    visited.add(neighbor)

            
            if endWord in visited:
                break

        # we want the length of the path (including the beginWord)
        return steps + 1 if endWord in visited else 0

    
    def ladderLength2(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Pairwise Comparison

        O(n^2 * L), time to build adjacency list
        O(n), space to store adjacency list
        """
        if endWord not in wordList:
            return 0
        
        if beginWord not in wordList:
            wordList.append(beginWord)

        adj_list = defaultdict(list)

        for i in range(len(wordList)):

            for j in range(i + 1, len(wordList)):
                diff = 0

                for c1, c2 in zip(wordList[i], wordList[j]):
                    if c1 != c2:
                        diff += 1

                    if diff > 1:
                        break

                if diff == 1:
                    adj_list[wordList[i]].append(wordList[j])
                    adj_list[wordList[j]].append(wordList[i])

        # bfs to find shortest path
        q = deque([beginWord])
        visited = set([beginWord])
        steps = 0

        while q:
            steps += 1

            for _ in range(len(q)):
                cur = q.popleft()

                for neighbor in adj_list[cur]:
                    if neighbor in visited:
                        continue

                    q.append(neighbor)
                    visited.add(neighbor)

            
            if endWord in visited:
                break

        # we want the length of the path (including the beginWord)
        return steps + 1 if endWord in visited else 0
