class Solution:
    def reverseWords(self, s: str) -> str:
        res = [] 
        words = s.split()

        for word in words:
            res.append(word[::-1])
        
        return " ".join(res)