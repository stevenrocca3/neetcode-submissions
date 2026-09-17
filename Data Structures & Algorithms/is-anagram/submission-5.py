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
            for i in t:
                if i in seen:
                    seen[i] -= 1
                else:
                    return False
            if all(i == 0 for i in seen.values()):
                return True
            return False