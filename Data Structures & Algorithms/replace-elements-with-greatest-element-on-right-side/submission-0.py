class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = -1
        res = [0] * len(arr)

        for i in range(len(arr) - 1, -1, -1):
            tmp = greatest
            greatest = max(greatest, arr[i])
            res[i] = tmp

        return res

