class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        map = {}
        for i, num in enumerate(nums):
            c = target - num
            if c in map:
                return [map[c], i]
            map[num] = i
        return []   