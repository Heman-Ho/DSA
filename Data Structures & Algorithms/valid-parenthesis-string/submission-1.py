class Solution:
    def checkValidString(self, s: str) -> bool:
        # cache holds tuple (i, num_open)
        cache = {}

        def dfs(i, num_open):
            if (i, num_open) in cache:
                return cache[(i, num_open)]

            # base case for success:
            if i == len(s) and num_open == 0:
                cache[(i, num_open)] = True
                return True
            
            # base case for failure:
            if num_open < 0 or (i == len(s) and num_open > 0):
                cache[(i, num_open)] = False
                return False
            
            cur_item = s[i]
            if cur_item == '(':
                res = dfs(i+1, num_open + 1)
            elif cur_item == ')':
                res = dfs(i+1, num_open - 1)
            else:  
                res = dfs(i+1, num_open + 1) or dfs(i+1, num_open - 1) or dfs(i+1, num_open)
            cache[(i, num_open)] = res
            return res

        return dfs(0, 0)
            
            
