class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # true if duplicate
        # false if not
       return len(nums)!= len(set(nums))