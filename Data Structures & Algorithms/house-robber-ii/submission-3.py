class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if nums is None:
            return 0
        if len(nums) == 1:
            return nums[0]
        def temp_func(nums: List[int]) -> int:
            pre1, pre2 = 0,0
            for n in nums:
                g = max(pre2 + n, pre1)
                pre2 = pre1
                pre1 = g
            return g

        f = temp_func(nums[:-1])
        d = temp_func(nums[1:])
        return max(f,d)    
        