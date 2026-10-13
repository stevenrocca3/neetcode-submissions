class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        result = [0] * (n+1)
        for i, k in enumerate(nums):
            if k in result and k:
                return True
            else:
                result.append(k)
        return False
        