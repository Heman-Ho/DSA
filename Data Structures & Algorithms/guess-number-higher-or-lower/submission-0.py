# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n

        while True:
            attempt = (l + r) // 2
            state = guess(attempt)
            if state == 0:
                return attempt
            if state == 1:
                l = attempt + 1
            else:
                r = attempt - 1
            
        