class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        arr = []
        for num, count in freq.items():
            arr.append([count, num])
        arr.sort()

        ans = []
        while len(ans) < k:
            ans.append(arr.pop()[1])
        return ans