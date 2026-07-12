import re

class Solution:
    def isPalindrome(self, s: str) -> bool:

    
        new_s = []
        # preprocess
        for letter in s:
            if re.match("[a-zA-Z0-9]", letter):
                new_s.append(letter.lower())
        l = 0
        r = len(new_s) - 1
        # print(new_s)
        while l < r:
            if new_s[l] != new_s[r]:
                return False
            l += 1
            r -= 1
        return True
