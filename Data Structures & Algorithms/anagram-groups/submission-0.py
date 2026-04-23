class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        listend =[]
        used = [False] * len(strs)
        for i in range(len(strs)):
            if used[i] != True:
                x = ''.join(sorted(strs[i]))
                used[i] = True
                listi = [strs[i]]
                for j in range(i+1, len(strs)):
                    if used[j] != True:
                        y = ''.join(sorted(strs[j]))
                        if str(x) == str(y):
                            listi.append(strs[j])
                            used[j] = True
                listend.append(listi)
        return listend
            

        