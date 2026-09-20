class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # turning list to set in python removes duplicates
        return len(nums) != len(set(nums))