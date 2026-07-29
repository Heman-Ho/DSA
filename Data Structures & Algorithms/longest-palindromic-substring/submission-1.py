class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_l = 0
        longest_r = 0

        if not s:
            return None

        # Case the longest palindrome is odd:
        # Iterate through each character, treating each as the new center
        for i in range(len(s)):
            l = i - 1
            r = i + 1
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                if r - l > longest_r - longest_l:
                    longest_r = r
                    longest_l = l
                l -= 1
                r += 1

        # Case the longest palindrome is even:
        # Iterate through each character, if s[i] == s[i+1] then treat those two characters as the middle of the palindrome
        for i in range(len(s)):
            l = i
            r = i + 1
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                if r - l > longest_r - longest_l:
                    longest_r = r
                    longest_l = l
                
                l -= 1
                r += 1
        return s[longest_l:longest_r + 1]
