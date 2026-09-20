class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
            
        # Sort keys based on their frequency count (reverse=True for highest first)
        sorted_elements = sorted(seen.keys(), key=lambda x: seen[x], reverse=True)
        
        # Return the top k elements
        return sorted_elements[:k]