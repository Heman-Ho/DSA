class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # keep a monotonically decreasing queue
        q = deque()
        res = []
        l = 0

        # 1, 2, 1, 0, 4, 2, 6
        # [1, 2, 3]  ==> [2, 1, 0]
        # res = [2, ]
        for r, num in enumerate(nums):
            while q and num >= nums[q[-1]]:
                q.pop()
            q.append(r)

            # remove element from q if it's out of range
            if q and q[0] < r - k + 1:
                q.popleft()

            if r + 1 >= k:
                res.append(nums[q[0]])
            
        return res