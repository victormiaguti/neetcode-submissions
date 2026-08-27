class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zeros = 1, 0
        res = []
        for num in nums:
            if num == 0:
                zeros += 1
                continue
            prod *= num
        for i in range(len(nums)):
            if zeros > 1:
                res.append(0)
            elif zeros == 1:
                if nums[i] == 0:
                    res.append(prod)
                else:
                    res.append(0)
            else:
                res.append(prod//nums[i])
        return res