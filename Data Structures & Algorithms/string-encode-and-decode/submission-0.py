class Solution:

    def encode(self, strs: List[str]) -> str:
        x = ""
        for i in strs:
            x = x + str(len(i)) +'#' + i
        return x

    def decode(self, s: str) -> List[str]:
        y, i = [], 0

        while i < len(s):
            f = i
            while s[f] != '#':
                f += 1
            length = int(s[i:f])
            d = s[f+1: f+1+length]
            y.append(d)
            i = f+1+length
        return y




        
