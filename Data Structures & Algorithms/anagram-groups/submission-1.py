from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list) # every new key automatically gets an empty list

        for s in strs:
            count = [0] * 26 # a spot for every letter of alphabet

            for char in s:
                #iterate through every character in curr strng
                count[ord(char) - ord('a')] += 1 # ord converts char to num  to correspond w groups list index

            groups[tuple(count)].append(s) # add as tuple simce its immutable instead of list

        return list(groups.values())