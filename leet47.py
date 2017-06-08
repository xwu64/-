class Solution(object):

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()

        def helper(nums):
            if len(nums) <2:
                return [nums]
            length = len(nums)
            i=0
            result = []
            for i in range(length):
                if i>0 and nums[i] == nums[i-1]:
                    continue
                tmp = helper(nums[:i]+nums[i+1:])
                for each in tmp:
                    result.append([nums[i]]+each)
            return result
        return helper(nums)
