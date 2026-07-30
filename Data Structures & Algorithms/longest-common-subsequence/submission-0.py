class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Let A[i,j] represent the longest common subsequence between the last i letters of text1 and the last j letters of text2
        # lcs[i,j] = 
        # Case 1: text1[i] == text2[j] => lcs[i,j] = 1 + lcs[i+1,j+1]
        # Case 2: Text1[i] != text2[j] => lcs[i,j] = max(lcs[i+1,j], lcs[i, j+1])
        if not text1 or not text2:
            return 0

        ROWS = len(text1)
        COLS = len(text2)

        lcs = [[0] * (COLS+1) for _ in range(ROWS+1)]
        
        for r in range(ROWS-1, -1, -1):
            for c in range(COLS-1, -1, -1):
                print(f"{text1[r]}, {text2[c]}")
                if text1[r] == text2[c]:
                    lcs[r][c] = 1 + lcs[r+1][c+1]
                else:
                    lcs[r][c] = max(lcs[r+1][c], lcs[r][c+1])
        print(lcs)
        return lcs[0][0]