from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurence = defaultdict(int)
        for i, c in enumerate(s):
            last_occurence[c] = i
        res = []

        partition_end = 0
        partition_start = 0
        for i, c in enumerate(s):
            partition_end = max(partition_end, last_occurence[c])

            if i == partition_end:
                res.append(partition_end - partition_start + 1)
                partition_start = partition_end + 1

        return res