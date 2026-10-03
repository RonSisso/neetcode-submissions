class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)
        product = 1
        for i in range (1, len(nums)):
            product *= nums[i-1]
            left[i] = product
        product = 1
        for i in range (len(nums) -2, -1, -1):
            product *= nums[i+1]
            right[i] = product
        ans = [left[i] * right[i] for i in range(len(nums))]
        return ans
