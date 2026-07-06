class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter = {}

        for letter in s:
            counter[letter] = counter.get(letter, 0) + 1
        
        for letter in t:
            counter[letter] = counter.get(letter, 0) - 1
        
        values = set(counter.values())
        print(values)
        if len(values) != 1:
            return False
        else:
            if 0 in values:
                return True
            return False
    