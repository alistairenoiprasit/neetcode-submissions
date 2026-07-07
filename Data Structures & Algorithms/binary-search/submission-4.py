class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        hi = len(nums) - 1
        low = 0

        while low <= hi:
            mid = low + ((hi - low) // 2)
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                hi = mid - 1
            elif target > nums[mid]:
                low = mid + 1
        return -1