from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for string in strs:
            key = tuple(sorted(string))
            anagrams[key].append(string)
        return list(anagrams.values())

