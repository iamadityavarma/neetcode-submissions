class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        s = []
        test = {}

        for i in nums:
            test[i] = 1+ test.get(i, 0)

        sorted_test = sorted(test.items(), key = lambda item:item[1], reverse = True)

        for i in range(k):
            x, y = sorted_test[i]
            s.append(x)
        return s
        
        