class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sortnum = sorted(nums)
        print(sortnum)

        i = 0
        j = len(nums)-1

        diff = {}
        ans = []
        for i in range(0,len(nums)):
            difference = target - nums[i]
            if difference not in diff:
                diff[nums[i]] = i
            elif difference in diff:
                ans.append(i)
                ans.append(diff[difference])
        return(sorted(ans))