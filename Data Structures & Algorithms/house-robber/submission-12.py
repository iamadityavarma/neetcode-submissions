class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_1, prev_2 = 0, 0

        for i in nums:
            f = max(prev_2 + i, prev_1)
            prev_2 = prev_1
            prev_1 = f
        return prev_1



            
