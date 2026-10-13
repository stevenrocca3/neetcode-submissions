class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        result = [0] * (n+1)
        for i, k in enumerate(nums):
            if k in result and k != 0:
                return True
            else:
                result[i] += k
        return False
        