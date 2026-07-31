class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or not strs[0]:
            return ""

        for i, common_letter in enumerate(strs[0]):
            for string in strs[1:]:
                if i >= len(string) or string[i] != common_letter:
                    return(strs[0][:i])
        return strs[0]