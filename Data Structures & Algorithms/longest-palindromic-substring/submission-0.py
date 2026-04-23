class Solution:
    def longestPalindrome(self, s: str) -> str:
        best = ""
        def recursionState(l,r):
            while l >= 0 and r<(len(s)) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        for i in range(len(s)):
            # odd
            left,right = i,i
            output = recursionState(left,right)
            if len(output) > len(best):
                best = output
            #even
            left,right = i,i+1
            output = recursionState(left,right)
            if len(output) > len(best):
                best = output

        return best