class Solution:
    def countBits(self, n: int) -> List[int]:
        # 0 1 1 2 1 2 2 3 1 2 2 3 2 3 3 4 1 
        res = []
        for i in range(n+1):
            # count the number of 1s in bin(i)
            cur_num = i
            num_ones = 0
            while cur_num:
                cur_num &= (cur_num - 1) # removes the rightmost set bit
                num_ones += 1
            res.append(num_ones)
        return res