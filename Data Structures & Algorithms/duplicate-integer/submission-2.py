class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if (len(nums) <= 1):
            return False
        sort_l = sorted(nums)
        prev = sort_l[0]
        for num in sort_l[1:]:
            if num == prev:
                return True
            prev = num
        return False