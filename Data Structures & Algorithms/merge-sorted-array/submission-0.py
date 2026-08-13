class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1

        # use 3 pointers merge in reverse order
        for i in range(len(nums1) - 1, -1, -1):
            if p2 < 0:
                return
            if p1 < 0 or nums1[p1] < nums2[p2]:
                nums1[i] = nums2[p2]
                p2 -= 1
            else:
                nums1[i] = nums1[p1]
                p1 -= 1
          
        return