class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        groups = [1] * len(nums)
        prefix = 1
        # [1,2,3,4]
        for i, num in enumerate(nums):
            groups[i] *= prefix
            prefix *= num
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            groups[i] *= suffix
            suffix *= nums[i]
        return groups


        