class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        trail_1, trail_2 = 0, 0  # dp[i-1], dp[i-2]
        for n in nums:
            new_val = max(trail_1, trail_2 + n)
            trail_2 = trail_1
            trail_1 = new_val
        return trail_1

            
