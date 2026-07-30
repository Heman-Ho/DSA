class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        A = [0] * (amount + 1)
        A[0] = 1
        
        for coin in coins:
            for i in range(len(A)):
                if i - coin >= 0:
                    A[i] += A[i-coin]
        print(A)
        return A[-1]