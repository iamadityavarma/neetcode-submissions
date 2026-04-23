class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        counter = 0
        nums_length = len(nums)
        x = []
        while counter < nums_length:
            product = 1
            for i in range(len(nums)):
                if i != counter:
                    product = product * nums[i]
            x.append(product)
            counter += 1 
        return x   



        


        