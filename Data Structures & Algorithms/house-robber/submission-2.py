class Solution:
    def rob(self, nums: List[int]) -> int:
        cost = [-1] * len(nums)
        def dfs(i):
            if (i) >= len(nums):
                return 0
            if cost[i] != -1:
                return cost[i]
            cost [i] =  max(nums[i] + dfs(i+2), dfs(i+1))
            return cost[i]
        return dfs(0)


        