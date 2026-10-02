class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry = 0

        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0 or carry > 0:
            digitA = int(a[i]) if i >= 0 else 0
            digitB = int(b[j]) if j >= 0 else 0

            newDigit = digitA ^ digitB ^ carry
            res.append(str(newDigit))
            carry = (digitA + digitB + carry) // 2

            i -= 1
            j -= 1

        res.reverse()
        return ''.join(res)