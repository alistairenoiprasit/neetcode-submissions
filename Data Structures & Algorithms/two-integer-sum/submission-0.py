class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counter = {}

        for i, n in enumerate(nums):
            other_val = target - n
            in_dict = counter.get(other_val, -1)
            if (in_dict != -1):
                return [in_dict, i]

            counter[n] = i
