class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
       
        buff = [(val, letter) for letter, val in counts.items()]
        res = []
        buff.sort(reverse=True)
        
        for val, letter in buff:
            for _ in range(val):
                res.append(letter)
            
        
        return "".join(res)