from collections import defaultdict
from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        ufds = UnionFind(len(accounts))
        # owners of emails, 
        # each email is mapped to an account id (index in accounts) 
        owner: dict[str, int] = {} 

        for i, account in enumerate(accounts):
            # emails for accounts are stored from index 1 onwards
            for email in account[1:]:
                if email in owner:
                    ufds.union(i, owner[email])

                owner[email] = i

        # track unique persons
        # each unique person will be the root of their own disjoint subtree
        persons: dict[int, List[str]] = defaultdict(list) 
        for email in owner:
            persons[ufds.find(owner[email])].append(email)

        return [
            # [name] + sorted(emails)
            [accounts[acc_id][0]] + sorted(emails)
            for acc_id, emails in persons.items()
        ]

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find(self, val):
        if self.parent[val] == val:
            return val

        self.parent[val] = self.find(self.parent[val])
        return self.parent[val]

    def union(self, u, v):
        x, y = self.find(u), self.find(v)

        if x == y:
            return

        if self.size[x] > self.size[y]: # make x the new root
            self.parent[y] = x
            self.size[x] += self.size[y]
        else: # self.size[x] <= self.size[y] # make y the new root
            self.parent[x] = y
            self.size[y] += self.size[x]
