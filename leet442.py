class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def swap(i, j, nums):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        i = 0
        length = len(nums)
        result = []
        while i < length:
            if nums[i] == 0:
                i+=1
                continue
            if i == nums[i]-1:
                i+=1
                continue
            else:
                if nums[i] == nums[nums[i]-1]:
                    result.append(nums[i])
                    nums[i] = 0
                    i+=1
                else: swap(i, nums[i]-1, nums)
        return result
