import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # Greedily add to the new string the letter that can be used the most and does not invalidate the happy string
        res = []

        # The max heap holds the letters that can be added to string without invalidating it
        max_heap = [(-a, "a"), (-b, "b"), (-c, "c")]
        heapq.heapify(max_heap)

        disable = (1, "#")
        print(max_heap)
        while max_heap:
            # Add the first item in the max heap to res
            count, char = heapq.heappop(max_heap)
            if count >= 0:
                continue
        
            res.append(char)
            count += 1

            # If there was a letter disabled, reenable it by pushing it to the heap
            if disable[0] < 0:
                heapq.heappush(max_heap, disable)
                disable = (1, "#")
            
            # if the previous 2 letters were the same letter, we disable it because we can't have 3 in a row
            if len(res) >= 2 and char == res[-2]:
                disable = (count, char)
            else:
                heapq.heappush(max_heap, (count, char))
        
        return "".join(res)