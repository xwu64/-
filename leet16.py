class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result = 999999
        length = len(nums)

        for i in xrange(length):
        	start = i+1
        	end = length-1
        	while end>start:
        		gap = nums[start]+nums[end]+nums[i]-target

        		if (abs(target - result) > abs(gap)):
        		    result = nums[start]+nums[end]+nums[i]
        		if gap > 0:
        			end-=1
        		elif gap < 0:
        			start+=1
        		else:
        			return target

        return result
