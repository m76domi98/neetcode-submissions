class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {} # hash map to contain everything we've gone through just in case we've alr seen complement
        for i, num in enumerate(nums): # we use enumerate so we dont need a counter var and we can get the val))
            complement = target - num # get the other num we looking for
            if complement in seen:
                return [seen[complement], i] # handle we've alr found complement case
            seen[num] = i # we havenet seen complement yet, so we ctn iterating
        return [] # handle nt found case
        