class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # case 1: different lengths - auto fail
        if (len(s) != len(t)):
            return False;

        char_counts = {} # initailzie hashmap that adds each character and the count of it
        
        # we can loop through s which we checked is same length as t to go through all letters
        # so this would be o(n)
        for i in range (len(s)):
            # make the key the letter. in s, +1 if it appears
            char_counts[s[i]] = char_counts.get(s[i], 0) + 1 #the 0 is backup value if it doesnt alr exist, and uses get so it doesnt fail if the key isnt found
            char_counts[t[i]] = char_counts.get(t[i],0) -1 # subtracts if found in t so then itll be 0 if its found in both

        # add up all the values
        for count in char_counts.values():
            if count != 0:
                return False
        
        return True;

    


        