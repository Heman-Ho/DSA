from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts_to_string = defaultdict(list)
        for string in strs:
            counts = [0] * 26
            for c in string:
                counts[ord(c) - ord('a')] += 1
            counts_to_string[tuple(counts)].append(string)
        
        return [group for group in counts_to_string.values()]