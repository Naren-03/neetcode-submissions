class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        for i in range(0,len(nums)):
            difference = target - nums[i]
            if difference not in diff:
                diff[nums[i]] = i
            elif difference in diff:
                return sorted([i,diff[difference]])
