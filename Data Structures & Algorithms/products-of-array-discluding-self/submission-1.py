class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force?
        # we do everything before
        n = len(nums)
        output = [1] *n
        prefix =1# start at one so we dont change any values we multiply by, and no prefix to first one
        for i in range (n):
            output[i] = prefix
            prefix *= nums[i]
        
        suffix = 1 # dont change values, and last one doesnt
        for i in range (n -1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]
        
        return output

        # then multiply by everything after
            
            
        