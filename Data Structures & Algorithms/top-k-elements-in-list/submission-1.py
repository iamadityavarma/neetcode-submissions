class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countval = {}
        x = []
        for i in nums:
            countval[i] = 1 + countval.get(i, 0)
        r = dict(sorted(countval.items(), key= lambda x:x[1], reverse= True)[:k])
        for d in r.keys():
            x.append(d)
        return x

        