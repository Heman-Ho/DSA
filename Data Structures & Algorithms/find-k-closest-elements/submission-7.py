class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k > len(arr):
            return arr

        # Use a binary search to find the insert position of x in the arr
        l, r = 0, len(arr) - 1
        while l < r:
            m = (l+r)//2
            if arr[m] == x:
                l = m
                break
            if arr[m] > x:
                r = m 
            else:
                l = m + 1
            
  
        l, r = l - 1, l
        # The window is exclusive to the numbers that we need in the res

        # use 2 pointers to loop through the neighbours of the insert position - 
        # one going left one going right, and shifting the pointer, whose value is closest to x
        while r - l + 1 < k + 2:
            print(f"r: {r}, l: {l}")
        
            if r == len(arr):
                return arr[r-k:]
            if l == -1:
                return arr[:k]
            if abs(x - arr[l]) <= abs(x - arr[r]):
                l -= 1
            else: 
                r += 1
           
        return arr[l+1:r]


        # l = -1, r = len(arr) 