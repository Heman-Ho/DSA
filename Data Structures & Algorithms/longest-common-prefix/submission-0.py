class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or not strs[0]:
            return ""

        # Use a common pointer and loop through all strs
        i = 0
        while True:
            if i >= len(strs[0]):
                return strs[0]
            common_letter = strs[0][i]

            for string in strs:
                if i >= len(string):
                    return string
                if string[i] != common_letter:
                    return string[:i]
            i += 1