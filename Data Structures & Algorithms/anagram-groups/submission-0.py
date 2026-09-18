class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        outputs = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            outputs[tuple(count)].append(s)
        return list(outputs.values())
