class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def checkPalindrome(l, r, deleted: bool):
            while l <= r:
                if s[l] != s[r] and deleted:
                    return False
                elif s[l] != s[r] and not deleted:
                    return checkPalindrome(l+1, r, True) or checkPalindrome(l, r-1, True)
                else:
                    l += 1
                    r -= 1
            return True
        
        return checkPalindrome(0, len(s) - 1, False)