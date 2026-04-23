class Solution:
    def countSubstrings(self, s: str) -> int:
        def palindromeCounter(l, r):
            count = 0
            while l>=0 and r < len(s) and s[l]==s[r]:
                count +=1
                l -=1
                r +=1
            return count
        oddCount,evenCount = 0,0
        for i in range(len(s)):
            oddCount += palindromeCounter(i,i)
            evenCount += palindromeCounter(i,i+1)
        totalCount = oddCount + evenCount
        return totalCount