class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t) and set(s) == set(t) and sorted(s) == sorted(t):
            return True
        else:
            return False


        