from collections import defaultdict, Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        # Get counts of all letters for each str using an array of size 26
        for string in strs:
            counts = [0] * 26
            for letter in string:
                idx = ord(letter) - ord('a')
                counts[idx] += 1

            # turn the array into a tuple use that tuple as a key to a dict
            anagrams[tuple(counts)].append(string)

        # loop through dict to produce output list
        return [strings for strings in anagrams.values()]