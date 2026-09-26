class UnionFind:
    def __init__(self):
        self.parent = {}
        self.size = defaultdict(lambda: 1)
    
    def find(self, i):
        if i not in self.parent:
            self.parent[i] = i
            return i

        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i == root_j: 
            return False
        
        if self.size[root_i] > self.size[root_j]:
            root_i, root_j = root_j, root_i

        self.parent[root_i] = root_j
        self.size[root_j] += self.size[root_i]
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind()
        email_to_name = {}

        for row in accounts:
            for email in row[1:]:
                email_to_name[email] = row[0]
            for email in row[2:]:
                uf.union(row[1], email)

        root_to_group = defaultdict(list)
        for email in email_to_name.keys():
            root_to_group[uf.find(email)].append(email)
        
        res = [] 

        for root, emails in root_to_group.items():
            res.append([email_to_name[root]] + sorted(emails))
        
        return res