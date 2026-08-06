class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        # aaaa, bbbb -> aabbbbaa
        # aa aa, bbbb | aaaa, bb bb
        # Let dp[i,j] represent whether s1[i:] and s2[j:] can interleave to make s3[i+j:]
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if ((i < len(s1) and s1[i] == s3[i+j] and dp[i+1][j]) or
                    (j < len(s2) and s2[j] == s3[i+j] and dp[i][j+1])):
                    dp[i][j] = True
      
        return dp[0][0]
                  
     