class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(i, memory=None): 
            if memory is None:
                memory = {}
            if i >= n:
                return i==n  
            if i in memory:
                return memory[i]     
            memory[i]= dfs(i+1, memory) + dfs(i+2, memory)
            return memory[i]
        return dfs(0)