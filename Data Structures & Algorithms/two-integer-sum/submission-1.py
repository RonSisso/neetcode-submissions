class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dic = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in nums_dic:
                return [nums_dic[comp], i]
            nums_dic[num] = i