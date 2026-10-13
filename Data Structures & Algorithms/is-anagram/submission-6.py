class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = set()
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            seen.add(s[i])
        for i in range(len(t)):
            if t[i] in seen:
                seen.remove(t[i])
        print(seen)
        if len(seen) == 0:
            return True
        return False
