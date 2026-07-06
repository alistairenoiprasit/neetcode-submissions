from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list)

        for s in strs:
            str_count = [0] * 26 # a .. z
            for c in s:
                str_count[ord(c) - ord("a")] += 1
            
            count[tuple(str_count)].append(s)
        return list(count.values())
