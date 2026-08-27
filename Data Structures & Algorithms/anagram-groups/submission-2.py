class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for string in strs:
            key = "".join(sorted(string))
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(string)
        ans = []
        for key, val in anagrams.items():
            ans.append(val)
        return ans

