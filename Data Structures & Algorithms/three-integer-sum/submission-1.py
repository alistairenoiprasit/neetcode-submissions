class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums = sorted(nums)
       
        for index, val in enumerate(nums):
            if index > 0 and val == nums[index - 1]:
                continue #same value
            l, r = index + 1, len(nums) - 1
            while (l < r):
                threeSum = val + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif (threeSum < 0):
                    l += 1
                else:
                    out.append([val, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return out