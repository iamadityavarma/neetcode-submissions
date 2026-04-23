class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        else:
            my_dict = {}
            for i in nums:
                if i in my_dict:
                    return True
                else:
                    my_dict[i] = i
            return False

        