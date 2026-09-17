class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        if len(t) != len(s):
            return False
        else:
            for i in s:
                if i in seen:
                    seen[i] += 1
                else:
                    seen[i] = 1
            result = set(seen.keys() - t)
            if not result:
                return True
            return False