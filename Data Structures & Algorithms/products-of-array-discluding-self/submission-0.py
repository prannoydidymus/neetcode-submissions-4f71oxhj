class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        if n == 0:
            return res

        left = [0] * n
        right = [0] * n

        product = 1
        for i in range(0,n):
            product *= nums[i]
            left[i] = product
        product = 1
        for i in range(n-1,-1,-1):
            product *= nums[i]
            right[i] = product
        res[0] = right[1]
        res[n-1] = left[n-2]

        for i in range(1,n-1):
            res[i] = left[i-1] * right[i+1]
        return res