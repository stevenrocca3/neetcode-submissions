class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for string in strs:
            result[tuple(sorted(string))].append(string)
        return list(result.values())
        