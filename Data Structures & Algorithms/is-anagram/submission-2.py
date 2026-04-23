class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = []
        b = []

        for i in s:
            a.append(i)

        for j in t:
            b.append(j)
        a.sort()
        b.sort()
        cnt = 0
        if len(a) == len(b):
            for w in range(len(a)):
                if a[w] != b[w]:
                    return False
                    #cnt +=1
                    #break
            return True
        else:
            return False

        