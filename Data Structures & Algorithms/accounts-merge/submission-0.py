class Solution:
    class UnionFind:
        def __init__(self, n):
            self.parent = list(range(n))
        
        def find(self, i):
            if self.parent[i] != i:
                self.parent[i] = self.find(self.parent[i])
            return self.parent[i]
        
        def union(self, i, j):
            root_i = self.find(i)
            root_j = self.find(j)
            self.parent[root_j] = root_i

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        res = []
        dsu = self.UnionFind(len(accounts))
        # Union every account index if they share the same email
        # How to find out the account indices that share the same email efficiently?
        # Create a hashmap email -> account index
        email_to_i = {}
        for i, account in enumerate(accounts):
            # loop through every email of every account. If email in hashmap, then we union the 2.
            for j in range(1, len(account)):
                email = account[j]
                if email in email_to_i:
                    dsu.union(email_to_i[email], i)
                else:
                    email_to_i[email] = i

        # Iterate through all emails in the hashmap and use the find operation of UF to group
        # each email to the leader of it's union's name
        i_to_emails = {}
        for email in email_to_i:
            account_index = email_to_i[email]
            leader_index = dsu.find(account_index)
            leader_name = accounts[leader_index][0]
            if leader_index in i_to_emails:
                i_to_emails[leader_index].append(email)
            else:
                i_to_emails[leader_index] = [email]

        for emails in i_to_emails.values():
            emails.sort()
        

        for i in i_to_emails:
            res.append([accounts[i][0]] + i_to_emails[i])

        return res
          
  
            

