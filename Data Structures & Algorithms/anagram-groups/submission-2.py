from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for c in strs:
            cnt = [0] * 26 #a to z
            for string in c:
                cnt[ord(string) - ord("a")] +=1           
            result[tuple(cnt)].append(c)
        
        return (list(result.values()))
        