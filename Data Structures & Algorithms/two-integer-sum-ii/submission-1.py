class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        # target  
        # 1 2 3 4 4 5 6 8
        # l           r

        while l < r:
            print(l, numbers[l], r, numbers[r])
            if (numbers[r] + numbers[l]) > target:
                r -= 1  
            elif (numbers[r] + numbers[l]) < target:
                l += 1
            else:
                return [l + 1, r + 1]
