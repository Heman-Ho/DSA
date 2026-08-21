class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        best = 1
        cur = 1

        if len(arr) <= 1:
            return len(arr)

        # 0 for neither increasing nor decreasing, 1 => increasing, 2 => decreasing
        prev_state = 0 

        for i in range(1, len(arr)):
            # If previous state was neither, then we start choose either increase or decrease
            if prev_state == 0:
                cur += 1
            elif prev_state == 1:
                if arr[i-1] > arr[i]:
                    cur += 1
                else: 
                    cur = 2
            else:
                if arr[i-1] < arr[i]: 
                    cur += 1
                else:
                    cur = 2

            if arr[i-1] < arr[i]:
                prev_state = 1
            elif arr[i-1] > arr[i]:
                prev_state = 2
            else:
                prev_state = 0
                cur = 1
            print(f"prev_state: {prev_state} best: {best}, cur: {cur}")
            best = max(best, cur)
        return best