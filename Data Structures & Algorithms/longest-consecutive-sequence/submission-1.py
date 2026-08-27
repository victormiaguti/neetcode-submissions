class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        max_so_far = 0
        for num in nums:
            seen.add(num)
        for num in seen:
            count = 0
            if num-1 not in seen:
                for i in range(len(seen)):
                    if num+i in seen:
                        count += 1
                    else:
                        break
            if count > max_so_far:
                max_so_far = count
        return max_so_far
